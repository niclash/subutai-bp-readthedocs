Ansible Role: readthedocs
=========================

This role will install a basic "Read the Docs" server instance.
For further information about "Read the Docs" see [readthedocs.org](https://readthedocs.org/).


Requirements
------------

Nothing.


Role Variables
--------------

    rtd_packages_pdf_output:
      - texlive
      - texlive-xetex
Additional packages to install if 'rtd_enable_pdf_output' is true

    rtd_enable_pdf_output: false
Enables the PDF output


Example Playbook
----------------

```
- hosts: doc-server
  roles:
    - { role: solutiondrive.readthedocs }
```


Maintainer
----------
solutionDrive DevOps <developer@solutiondrive.de>
