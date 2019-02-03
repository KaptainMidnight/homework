import json

def main():
    a = input("Enter name: ")
    my_json = open("data.json", "r", encoding="utf-8")
    json_data = json.load(my_json)
    for i in json_data["users"]:
        if a in i["name"]:
            print(i["phone"])


if __name__ == '__main__':
    main()
