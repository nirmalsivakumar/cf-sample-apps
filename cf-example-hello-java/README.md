cf-example-hello-java
=====================

Dependencies
-----

You need maven2 and a jdk installed e.g.

```
sudo apt-get install maven2 openjdk-6-jdk
```

Build
-----

```
mvn package
```

Deploy to Cloud Foundry
-----------------------------

```
cf push
```

> **Note**: For the time being we do not have a namespace concept for the trial landscape, hence app names are gobal. As such you may encounter the following error:
>
> `FAILED Server error, status code: 400, error code: 210003, message: The host is taken: hello-java`
>
> To fix that, please add a suffix or prefix (or change the entire name) to the `host` attribute within the [manifest.yml](/manifest.yml) file!

Run Locally
-----------

```
mvn package tomcat7:run
# in another shell call
curl http://localhost:8080/hello/
```

> **Note:** The trailing `/` is needed to see the response in the shell!
