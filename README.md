# tarsier-input-rethinkdb

rethinkdb input plugin for tarsier.


## install

```bash
pip install tarsier-input-rethinkdb
```

## configuration

```yaml
in:
  type: rethinkdb
  host: 127.0.0.1 # default
  port: 28015 # default
  db: test # default
  user: admin # default
  password: "" # default
  timeout: 20 # default
  # ssl:  # optional
  table: test # required
  time_condition: # required
    field: # time field
    duration: # time duration. you can use years, months, days, hours, minutes, seconds
      minutes: 3
```

