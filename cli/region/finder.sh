set -e
setup(){
  project="freetier-only"
  principal="cloud-region@freetier-only.iam.gserviceaccount.com"

  gcloud services enable cloudlocationfinder.googleapis.com --project $project
  gcloud projects add-iam-policy-binding $project --member serviceAccount:$principal --role roles/cloudlocationfinder.viewer
  gcloud components install alpha --quiet # require privilege
}
# param ref: https://cloud.google.com/location-finder/docs/reference/rest/v1alpha/projects.locations.cloudLocations#CloudLocation
search-territory(){
  # TODO
  cloud_provider="CLOUD_PROVIDER_AWS" # one of [CLOUD_PROVIDER_GCP, CLOUD_PROVIDER_AWS, CLOUD_PROVIDER_AZURE, CLOUD_PROVIDER_OCI]
  CLOUD_REGION="gcp-asia-east2"
  territory_code=$1 # a two-letter ISO 3166-1 alpha-2 code
  # query syntax ref: https://cloud.google.com/location-finder/docs/syntax
  gcloud alpha cloudlocationfinder cloud-locations search --source-cloud-location=$CLOUD_REGION \
    --query="cloud_provider=$cloud_provider AND cloud_location_type=CLOUD_LOCATION_TYPE_REGION AND territory_code=$territory_code"
    --limit=1
}
$@