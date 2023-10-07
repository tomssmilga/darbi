import pandas 
get_info=input()

try:
    fails = pandas.read_excel("description.xlsx", sheet_name="LookupAREA")
    filtered_fails = fails[fails['Description'] == get_info]
    if not filtered_fails.empty:
        area_code = filtered_fails['Area'].iloc[0]
        try:
            data = pandas.read_csv('data.csv')
            filtered_data = data[data['Area'] == area_code]
            total_sum = filtered_data['geo_count'].sum()
            print(total_sum)
        except FileNotFoundError:
            print("0")
    else:
        print("0")
except FileNotFoundError:
    print("0")
except Exception as e:
    print(f"{str(e)}")