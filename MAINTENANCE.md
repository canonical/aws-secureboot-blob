# Maintenance

Some info about maintaining this repository.

## New release

To do a new release

1. make sure everything is included in current `main` (eg. check for open PRs)
1. create a new tag. The tag should have the format of a serial (eg. `20230329`)
1. push the tag

Then the github action will create a new release including the binary blob.
