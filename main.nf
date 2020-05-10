params.bulk_files_folder = './cohort_data/bulk_data/**/*'
params.phenotypes_file = './cohort_data/cohort_phenotypes.csv'
params.math_operation = 'multiplication'

process sumBulkData {
  container 'python:latest'
  publishDir 'output'

  input:
  file phenotypesFile from Channel.fromPath(params.phenotypes_file)
  val phenotypicField from params.phenotypic_field
  val bulkField from params.bulk_field
  val mathOperation from params.math_operation
  file bulkFiles from Channel.fromPath( params.bulk_files_folder ).collect()

  output:
  file '*.csv'
  file '*.modified'

  script:
  template 'bulk_data_operations.py'

}