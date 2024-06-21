# Overview

We are leading with two problems:

1. Put assets - namespaces and VMs - into a hierarchy and manage permissions accordingly
2. Apply certain settings to a group of VMs.

## Personas

The personas are likely different:

1. Cluster Admin - Cares about managing access to and on assets
2. VM Owner - Cares about how the VMs are configured

## User Stories

Thus we can rephrase into the following user-stories:

1. As a cluster administrator I want to have a mechanism to logically group assets - namespaces and VMs - in order to manage permissions according to my organizational topology
2. As a Vm owner I want to have a mechanism to logically group VMs in order to apply the same configuratio to all VMs in this group ie. applying a cloud-init configuratoin

# Folders

Folders are not discussed jere. see folders/

# Commons

## User Stories
* As a user I want to manage multiple namespaces at once in order to inject my ssh key into all VMs created in my namespaces
