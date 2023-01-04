# GCP-collections
- Most Google Cloud APIs also support anonymous access to **public data** using API keys. However, API keys only identify the application, not the principal. When using API keys, the principal must be authenticated by other means.

## Hardware root of trust
- The first integrity check for Google servers uses a hardware root of trust.
### Datacenter Identity
- Each server in the data center has its own unique identity.
- This identity can be tied to the hardware root of trust and the software with which the machine boots
- This identity is used to authenticate API calls (Application Layer Transport Security (ALTS) system) to and from low-level management services on the machine.
- This identity is used for mutual server authentication and transport encryption.
