#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : python-dbusmock
Version  : 0.23.1
Release  : 3
URL      : https://files.pythonhosted.org/packages/3d/38/6c3dee0c66d7162e87c6faa489214f22437bc7e9bad83caf626f5c87acf6/python-dbusmock-0.23.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/3d/38/6c3dee0c66d7162e87c6faa489214f22437bc7e9bad83caf626f5c87acf6/python-dbusmock-0.23.1.tar.gz
Summary  : Mock D-Bus objects
Group    : Development/Tools
License  : LGPL-3.0 LGPL-3.0+
Requires: python-dbusmock-license = %{version}-%{release}
Requires: python-dbusmock-python = %{version}-%{release}
Requires: python-dbusmock-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
===============
        
        Purpose
        -------
        With this program/Python library you can easily create mock objects on D-Bus.
        This is useful for writing tests for software which talks to D-Bus services
        such as upower, systemd, logind, gnome-session or others, and it is hard
        (or impossible without root privileges) to set the state of the real services
        to what you expect in your tests.
        
        Suppose you want to write tests for gnome-settings-daemon's power plugin, or
        another program that talks to upower. You want to verify that after the
        configured idle time the program suspends the machine. So your program calls
        ``org.freedesktop.UPower.Suspend()`` on the system D-Bus.
        
        Now, your test suite should not really talk to the actual system D-Bus and the
        real upower; a ``make check`` that suspends your machine will not be considered
        very friendly by most people, and if you want to run this in continuous
        integration test servers or package build environments, chances are that your
        process does not have the privilege to suspend, or there is no system bus or
        upower to begin with. Likewise, there is no way for an user process to
        forcefully set the system/seat idle flag in logind, so your
        tests cannot set up the expected test environment on the real daemon.

%package license
Summary: license components for the python-dbusmock package.
Group: Default

%description license
license components for the python-dbusmock package.


%package python
Summary: python components for the python-dbusmock package.
Group: Default
Requires: python-dbusmock-python3 = %{version}-%{release}

%description python
python components for the python-dbusmock package.


%package python3
Summary: python3 components for the python-dbusmock package.
Group: Default
Requires: python3-core
Provides: pypi(python_dbusmock)

%description python3
python3 components for the python-dbusmock package.


%prep
%setup -q -n python-dbusmock-0.23.1
cd %{_builddir}/python-dbusmock-0.23.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1624044102
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/python-dbusmock
cp %{_builddir}/python-dbusmock-0.23.1/COPYING %{buildroot}/usr/share/package-licenses/python-dbusmock/f45ee1c765646813b442ca58de72e20a64a7ddba
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/python-dbusmock/f45ee1c765646813b442ca58de72e20a64a7ddba

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
