import csv
import googlemaps

def get_address(location, gmaps):
    # get address using gmaps api
    print(f'Obtaining address for {location["Location Name String"]}...', end = '')
    geocode_result = gmaps.geocode(f'{location["Location Name String"]}+{location["Neighborhood"]}+{location["City"]}')
    if geocode_result:
        location["Address"] = geocode_result[0]['formatted_address']
    else:
        print('Google Maps was unable to obtain an address for this location.')

def main():
    try:
        gmaps = None
        with(open("apikey.txt", mode="r")) as apikey_file:
            gmaps = googlemaps.Client(key=apikey_file.readline())

        with open("input_csv_files.txt", mode="r") as input_csv_files:
            for line in input_csv_files:
                filename = line.rstrip()
                print(f'Processing csv file {filename}.')
                column_names, output_rows = [], []
                # Read from specified csv file
                with open(f'{filename}.csv', mode='r', encoding='utf8') as csv_file:
                    csv_reader = csv.DictReader(csv_file)
                    line_count = 0
                    for row in csv_reader:
                        if line_count == 0:
                            column_names = row.keys()
                        line_count += 1
                        if not row["Address"]:
                            get_address(row, gmaps) # where the magic happens
                            output_rows.append(row)
                            print('Done.')
                        else:
                            print(f'Skipping {row["Location Name String"]}; address has already been obtained for this location.') 

                # Write to csv file
                with open(f"{filename}_output_addresses.csv", mode="w", encoding="utf8", newline="")  as output_csv_file:
                    csv_writer = csv.DictWriter(output_csv_file, fieldnames=column_names)
                    csv_writer.writeheader()
                    for row in output_rows:
                        csv_writer.writerow(row)
                print('Success.')
    except Exception as e:
        print('Extraction failed.', e)

if __name__ == "__main__":
    main()
