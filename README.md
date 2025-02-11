# aws-secureboot-blob

The `aws-secureboot-blob` creates a binary blob containing
a pre-filled variable store containing the UEFI Secure Boot keys.
This binary blob can then be used to boot a AWS EC2 instance
with secure boot enabled.

See also the [AWS documentation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/aws-binary-blob-creation.html).

## requirements

To be able to run `aws-secureboot-blob`, some software needs
to be installed:

```
sudo apt install --yes sbsigntool efitools
sudo snap install uefivars
```

## usage

To create the binary blob, do:

```
./aws-secureboot-blob
```

That will create the blob (by default for `amd64`) file called
`aws-uefiblob.bin`.

The blob can then be used during image registration. For details how
to create a new AMI based on an existing Ubuntu AMI, see the `test-instance` script.


## contributing

We welcome external contributions. Before proposing changes please
[create an issue](https://github.com/canonical/aws-secureboot-blob/issues/new?template=Blank+issue)
describing the request. This helps ensure we prioritize accordingly and avoid duplicating effort.

When a pull request is opened against this repository it is expected that it will fail
when initiated from a fork. The pipeline tests secureboot in a Canonical provided AWS account,
which is not allowed to be launched from a fork. Changes from external contributors will be manually tested
Maintainers of this repository should push their branches to origin to allow for end to end testing
in the pull request.
