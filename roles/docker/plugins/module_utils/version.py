# -*- coding: utf-8 -*-

# Copyright (c) 2021, Felix Fontein <felix@fontein.de>
# GNU General Public License v3.0+ (see LICENSES/GPL-3.0-or-later.txt or https://www.gnu.org/licenses/gpl-3.0.txt)
# SPDX-License-Identifier: GPL-3.0-or-later

"""Provide version object to compare version numbers."""

from __future__ import absolute_import, division, print_function
__metaclass__ = type


# Once we drop support for ansible-core 2.11, we can remove the try/except.

from ansible.module_utils.six import raise_from

try:
    from ansible.module_utils.compat.version import LooseVersion, StrictVersion  # noqa: F401, pylint: disable=unused-import
except ImportError:
    try:
        from distutils.version import LooseVersion, StrictVersion  # noqa: F401, pylint: disable=unused-import
    except ImportError as exc:
        msg = 'To use this plugin or module with ansible-core 2.11, you need to use Python < 3.12 with distutils.version present'
        raise_from(ImportError(msg), exc)
