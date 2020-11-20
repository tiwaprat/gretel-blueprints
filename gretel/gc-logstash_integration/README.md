## Logstash and Local Gretel NER Integration

Diving deeper into on-prem use cases, we set up a Logstash pipeline.  The pipeline routes records
through the Gretel NER Docker container and on to Elasticsearch.

### Services and pipeline

The `docker-compose.yaml` file defines the four services we have running: logstash, gretel_ner, elasticsearch and kibana.

The `logstash/logstash.conf` file defines a Logstash pipeline that directs records through the different services.

The `logstash` container listens for incoming records on port 8080 (`input.http` in logstash.conf).
Records are filtered through `gretel_ner` container as part of the Logstash pipeline (`filter.http` in logstash.conf).
Records are dumped into `elasticsearch` container at the end of the Logstash pipeline
(`output.elasticsearch` in logstash.conf).  Now you can view the records in kibana.

Before you run the last step in the notebook and tear down the containers, go to http://localhost:5601/ .
Set up `logstash*` as an Index Pattern.  For fun, try `body.label: "ip_address"` as a KQL query.
You should see the handful of rare records with an IP Address in the ExtraText field.
