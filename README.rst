Open edX Platform
#################
| |License: AGPL v3| |Status| |Python CI|

.. |License: AGPL v3| image:: https://img.shields.io/badge/License-AGPL_v3-blue.svg
  :target: https://www.gnu.org/licenses/agpl-3.0

.. |Python CI| image:: https://github.com/openedx/edx-platform/actions/workflows/unit-tests.yml/badge.svg
  :target: https://github.com/openedx/edx-platform/actions/workflows/unit-tests.yml

.. |Status| image:: https://img.shields.io/badge/status-maintained-31c653

Purpose
*******
The `Open edX Platform <https://openedx.org>`_ is a service-oriented platform for authoring and
delivering online learning at any scale.  The platform is written in
Python and JavaScript and makes extensive use of the Django
framework. At the highest level, the platform is composed of a
monolith, some independently deployable applications (IDAs), and
micro-frontends (MFEs) based on the ReactJS.

This repository hosts the monolith at the center of the Open edX
platform.  Functionally, the edx-platform repository provides two services:

* CMS (Content Management Service), which powers Open edX Studio, the platform's learning content authoring environment; and
* LMS (Learning Management Service), which delivers learning content.

Documentation
*************

Documentation can be found at https://docs.openedx.org/projects/edx-platform.

Getting Started
***************

Installing and running an Open edX instance is not simple.  We strongly
recommend that you use a service provider to run the software for you.  They
have free trials that make it easy to get started:
https://openedx.org/get-started/

If you will be modifying edx-platform code, `Tutor`_ is
the community-supported Docker-based Open edX distribution, both for production and
local development. The goal of Tutor is to make it easy to deploy, customise,
upgrade and scale your Open edX installation.

You can read more about getting up and running with a Tutor deployment
at the `Site Ops home on docs.openedx.org`_.

.. _Tutor: https://github.com/overhangio/tutor
.. _Site Ops home on docs.openedx.org: https://docs.openedx.org/en/latest/site_ops/index.html

Dependencies
============

In order to build and run this code you'll need the following available on your
system:

Interperters/Tools:

* Python 3.8

* Node 16

Services:

* MySQL 5.7

* Mongo 7.x

* Memcached

License
*******

The code in this repository is licensed under version 3 of the AGPL
unless otherwise noted. Please see the `LICENSE`_ file for details.

.. _LICENSE: https://github.com/openedx/edx-platform/blob/master/LICENSE


More about Open edX
*******************

See the `Open edX site`_ to learn more about the Open edX world. You can find
information about hosting, extending, and contributing to Open edX software. In
addition, the Open edX site provides product announcements, the Open edX blog,
and other rich community resources.

.. _Open edX site: https://openedx.org


Getting Help
************

If you're having trouble, we have discussion forums at
https://discuss.openedx.org where you can connect with others in the community.

Our real-time conversations are on Slack. You can request a `Slack
invitation`_, then join our `community Slack team`_.

For more information about these options, see the `Getting Help`_ page.

.. _Slack invitation: https://openedx.org/slack
.. _community Slack team: http://openedx.slack.com/
.. _Getting Help: https://openedx.org/getting-help


Issue Tracker
*************

We use Github Issues for our issue tracker. You can search
`previously reported issues`_.  If you need to report a bug, or want to discuss
a new feature before you implement it, please `create a new issue`_.

.. _previously reported issues: https://github.com/openedx/edx-platform/issues
.. _create a new issue: https://github.com/openedx/edx-platform/issues/new/choose


How to Contribute
*****************

Contributions are welcome! The first step is to submit a signed
`individual contributor agreement`_.  See our `CONTRIBUTING`_ file for more
information – it also contains guidelines for how to maintain high code
quality, which will make your contribution more likely to be accepted.

New features are accepted. Discussing your new ideas with the maintainers
before you write code will also increase the chances that your work is accepted.

Code of Conduct
***************

Please read the `Community Code of Conduct`_ for interacting with this repository.

Reporting Security Issues
*************************

Please do not report security issues in public. Please email
security@openedx.org.

.. _individual contributor agreement: https://openedx.org/cla
.. _CONTRIBUTING: https://github.com/openedx/.github/blob/master/CONTRIBUTING.md
.. _Community Code of Conduct: https://openedx.org/code-of-conduct/

People
******

The current maintainers of this repository can be found on `Backstage`_.

.. _Backstage: https://backstage.openedx.org/catalog/default/component/edx-platform

