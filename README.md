## Mailganer uploader

Small script that will upload users data (email, name, patronymic, surname) from the sqlite database to one single [mailganer.com]([https://link](https://mailganer.com/)) list.

<br>

Every single script run will pick one unprocessed user record from the **data.sqlite** database file, send it to list, that is setted up in **config.yaml** file, and then set *processed* field of this record to 'Y' as indication of uploaded data.

<br>

Script could be executed by simply calling
```bash
python3 mailganeruploader.py
```
Initially, script was designed to be called by cron, so it process only one record at a time.

<br>

Script will need **config.yaml** file to be provided to the same directory as the script. Its contents should look like following.
```yaml
api_key: {{mailhaner_api_key}}
source: {{mailganer_list_id}}
```

<br>

Also, you will need to provide **data.sqlite** file to the same directory as the script. Its contents should look like following.
|email         |name|patronymic|surname|processed|
|--------------|----|----------|-------|---------|
|name1@mail.com|Имя |Отчество  |Фамилия|         |
|name2@mail.com|Имя |Отчество  |Фамилия|         |
|...           |... |...       |...    |...      |
|nameN@mail.com|Имя |Отчество  |Фамилия|         |
Please note that field *processed* should be empty line '' for every user that are not uploaded to mailganer list yet.