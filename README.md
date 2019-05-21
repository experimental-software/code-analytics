# Code Analysis Utilities

## Metrics
- https://www.sonarsource.com/resources/white-papers/cognitive-complexity.html
- https://github.com/aim42/aim42/issues/236



## Sonar

```
docker run -d --name sonarqube -p 9000:9000 -p 9092:9092 sonarqube
cd $REPO
./gradlew sonarqube -Dsonar.host.url=http://localhost:9000
```

### API

List all available projects:
```
http GET http://localhost:9000/api/components/search?qualifiers=TRK
```

### Adding custom measures

- https://docs.sonarqube.org/latest/instance-administration/custom-measures/
- https://stackoverflow.com/questions/34099200/is-there-a-way-to-add-additional-code-metrics-in-sonarqube-without-having-to-wri/34135183
- https://stackoverflow.com/questions/11731155/how-to-customize-metrics-in-sonar
- https://jira.sonarsource.com/browse/SONAR-11184

## Code charta
- https://github.com/MaibornWolff/codecharta/blob/master/README.md#download

Create JSON file from a Sonarcube project:
```
ccsh sonarimport http://localhost:9000 $PROJECT_KEY > /tmp/sonar.json
```

Create JSON file from Codemaat:
```
git log --all --numstat --date=short --pretty=format:'--%h--%ad--%aN' --no-renames > /tmp/gitlog.txt
java -jar ~/bin/code-maat.jar --log /tmp/gitlog.txt --version-control git2 --analysis revisions > /tmp/codemaat_revisions.csv
ccsh codemaatimport /tmp/codemaat_revisions.csv > /tmp/codemaat_revisions.json
```

Merge two JSON files:
```
atom /tmp # sync project names manually
ccsh merge /tmp/codemaat_revisions.json /tmp/sonar.json > /tmp/merged.json
```

Run visualization service:
```
codecharta-visualization
```


## Code Maat

https://github.com/adamtornhill/code-maat

### Setup MacOS

```
brew install leiningen

git clone git@github.com:adamtornhill/code-maat.git
cd code-maat
lein uberjar
cp target/code-maat-1.1-SNAPSHOT-standalone.jar ~/bin/code-maat.jar
```

### Usage

Hello World:
```
cd $REPO
git log --all --numstat --date=short --pretty=format:'--%h--%ad--%aN' --no-renames > /tmp/gitlog.txt
java -jar ~/bin/code-maat.jar --log /tmp/gitlog.txt --version-control git2
```

Show help:
```
java -jar ~/bin/code-maat.jar --help
```

### Available analysis options

```
java -jar ~/bin/code-maat.jar --log /tmp/gitlog.txt --version-control git2 --analysis ${ANALYSIS_NAME}
```

| Analysis | Description |
|--------|-------------|
| abs-churn | date,added,deleted,commits |
| age | entity,age-months |
| author-churn | author,added,deleted,commits |
| authors | entity,n-authors,n-revs |
| communication | author,peer,shared,average,strength |
| coupling | entity,coupled,degree,average-revs |
| entity-churn | entity,added,deleted,commits |
| entity-effort | entity,author,author-revs,total-revs |
| entity-ownership | entity,author,added,deleted |
| fragmentation | entity,fractal-value,total-revs |
| identity | author,rev,date,entity,message,loc-added,loc-deleted |
| main-dev | entity,main-dev,added,total-added,ownership |
| main-dev-by-revs | entity,main-dev,added,total-added,ownership |
| messages |  |
| refactoring-main-dev | entity,main-dev,removed,total-removed,ownership |
| revisions | entity,n-revs |
| soc | Sum of coupling |
| summary | Count the number of commits, entities, entities changed, and authors |

## References

- [Codecharta](https://maibornwolff.github.io/codecharta/)
- [Software Design X-Rays](https://pragprog.com/book/atevol/software-design-x-rays)
- https://www.sonarqube.org/
- https://github.com/ishepard/pydriller

