# Source the file with the values of CODECOV_TOKEN and STATIC_ANALYSIS token
include venv/tokens
# Set upload target as localhost
CODECOV_HOST=http://localhost

do-upload:
	codecovcli --url=$(CODECOV_HOST) create-commit --token=$(CODECOV_TOKEN)
	codecovcli --url=$(CODECOV_HOST) create-report --token=$(CODECOV_TOKEN)
	codecovcli --url=$(CODECOV_HOST) --codecov-yml-path=codecov_cli.yml do-upload --token=$(CODECOV_TOKEN) --plugin=pycoverage --flag unit-with-labels

static-analysis:
	codecovcli --url=$(CODECOV_HOST) static-analysis --token=$(STATIC_ANALYSIS) --folders-to-exclude=venv 

label-analysis:
	codecovcli --url=$(CODECOV_HOST) label-analysis --token=$(STATIC_ANALYSIS)