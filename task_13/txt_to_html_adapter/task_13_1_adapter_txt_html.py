"""
Implement adapter pattern from_txt_to_html
for example, we have a such structure in txt:
name,surname,age,salary
Bohdan,Dovbysh,28,100

I want to see:
<name>Bohdan</name>
<surname>Dovbysh</surname>
"""


class DataAdapter:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def txt_to_html(self):
        with open(self.file_path) as file:
            lines = file.readlines()
        tags_txt = lines[0].replace('\n', '')
        common_data = lines[1:]
        user_data = [item.replace('\n', '').split(',') for item in
                     common_data]
        tags = tags_txt.split(',')

        result = ""
        for data in user_data:
            for index in range(len(tags)):
                result += f"<{tags[index]}>{data[index]}" \
                          f"</{tags[index]}>\n"
        return result


if __name__ == '__main__':
    data_file = DataAdapter('data_to_html.txt').txt_to_html()
    print(data_file)
