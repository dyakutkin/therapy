# Therapy assignment

## Prerequisites
- `make`
- `Docker` 1.13.0+
- `docker-compose`

## Usage
- `make run`
- Make direct API calls to `localhost:9000/calculate/`
- `make test`
- `make coverage`

## Rationale
The main idea in terms of approach was to treat substitution expressions as data in a generic way.

Why so?
- While it's not stated explicitly here, usually this kind of business requirements is a frequent subject of change in a real life situations;
- Can be managed by non-programmers if it's necessary;
- It fits a concept of expressions override/extension nicely.

Python is picked just because that's what I use day to day.
FastAPI is simple enough to provide basic http API capabilities without getting in the way.
All the other Python-related dependencies are regular widespread Python utilities packages.

There isn't any kind of DBMS or other dedicated data store, as it seems that it will only take some time to add it and won't really benefit in the context of the task in any way.
Substitution expressions data is stored in `./app/dump.json`, and can be tweaked there as well (just don't forget to restart the server).

Obviously, in a real life scenario it should be stored in a dedicated data store.
The choice of it would probably needs more context, but right now `MongoDB` seems like a great fit for it, as it's not really expected to see any kind of meaningful relations between the documents, but their structure might vary a lot depending on types and sized of expressions.