# Code Analysis Utilities

## Setup
### General infrastructure
- [Docker](https://docs.docker.com/install/)

### Code analysis tools
- [SonarCube](https://github.com/experimental-software/code-analytics/wiki/SonarCube#setup)
- [CodeMaat](https://github.com/experimental-software/code-analytics/wiki/CodeMaat#setup)
- [CodeCharta](https://github.com/experimental-software/code-analytics/wiki/CodeCharta#setup)

## Usage

```
function sonar_start() {
    docker run --env ES_JAVA_OPTS="-Xms750m -Xmx750m" -d -p 9000:9000 -p 9092:9092 \
    sonarqube
}

function sonar_list_projects() {
    http GET http://localhost:9000/api/components/search?qualifiers=TRK
}

function sonar_import_via_gradle() {
    ./gradlew sonarqube -Dsonar.host.url=http://localhost:9000
}

function sonar_export_json() {
    if [[ -n $1 ]]; then
        PROJECT_KEY=$1
        ccsh sonarimport http://localhost:9000 $PROJECT_KEY > /tmp/sonar.json
    else
        echo "Please provide the PROJECT_KEY as parameter."
    fi
}

function codemaat_export_gitlog() {
    # --since="3 month"
    git log --all --numstat --date=short --pretty=format:'--%h--%ad--%aN' --no-renames > /tmp/gitlog.txt
}

function codemaat_analyis() {
    if [[ -n $1 ]]; then
        ANALYSIS_NAME=$1

        java -jar ~/bin/code-maat.jar --log /tmp/gitlog.txt --version-control git2 \
        --analysis ${ANALYSIS_NAME} > /tmp/codemaat_analysis.txt

        cat /tmp/codemaat_analysis.txt
    else
        echo "Please provide the ANALYSIS_NAME as parameter. See https://github.com/experimental-software/code-analytics/wiki/CodeMaat#available-analysis-options"
    fi
}

function codemaat_enrich_sonar_json() {
    python ~/src/experimental-software/code-analytics/enrich_codecharta_data.py --sonar-json /tmp/sonar.json \
    --codemaat-csv /tmp/codemaat_analysis.txt

    echo "$?"
}
```


## Development

Run all unit tests:

```
python *.test.py
```

## Software metrics
- [Cognitive complexity](https://www.sonarsource.com/resources/white-papers/cognitive-complexity.html) | sonarsource.com
- [Monitor Debt: Which metrics?](https://github.com/aim42/aim42/issues/236) | github.com/aim42

## References

- [Codecharta](https://maibornwolff.github.io/codecharta/)
- [Software Design X-Rays](https://pragprog.com/book/atevol/software-design-x-rays)
- [SonarQube](https://www.sonarqube.org/)
- [PyDriller](https://github.com/ishepard/pydriller)
