# biosboot.py
# Device format classes for anaconda's storage configuration module.
#
# Copyright (C) 2011  Red Hat, Inc.
#
# This copyrighted material is made available to anyone wishing to use,
# modify, copy, or redistribute it subject to the terms and conditions of
# the GNU General Public License v.2, or (at your option) any later version.
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY expressed or implied, including the implied warranties of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General
# Public License for more details.  You should have received a copy of the
# GNU General Public License along with this program; if not, write to the
# Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA
# 02110-1301, USA.  Any Red Hat trademarks that are incorporated in the
# source code or documentation are not subject to the GNU General Public
# License and may only be used or replicated with the express permission of
# Red Hat, Inc.
#
# Red Hat Author(s): Dave Lehman <dlehman@redhat.com>
#

from parted import PARTITION_BIOS_GRUB

from ..size import Size
from .. import platform
from ..i18n import N_
from . import DeviceFormat, register_device_format

class BIOSBoot(DeviceFormat):
    """ BIOS boot partition for GPT disklabels. """
    _type = "biosboot"
    _name = N_("BIOS Boot")
    _udevTypes = []
    partedFlag = PARTITION_BIOS_GRUB
    _formattable = True                 # can be formatted
    _linuxNative = True                 # for clearpart
    _maxSize = Size(spec="2 MiB")
    _minSize = Size(spec="512 KiB")

    def __init__(self, *args, **kwargs):
        """
            :keyword device: path to the block device node
            :type device: str
            :keyword exists: whether the formatting exists
            :type exists: bool

            .. note::

                The 'device' kwarg is required for existing formats.
        """
        DeviceFormat.__init__(self, *args, **kwargs)

    @property
    def status(self):
        return False

    @property
    def supported(self):
        return isinstance(platform.platform, platform.X86)

register_device_format(BIOSBoot)

