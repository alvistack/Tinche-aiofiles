# Copyright 2022 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

Name: python-aiofiles
Epoch: 100
Version: 0.7.0
Release: 1%{?dist}
BuildArch: noarch
Summary: File support for asyncio
License: Apache-2.0
URL: https://github.com/Tinche/aiofiles/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
aiofiles is an Apache2 licensed library, written in Python, for handling
local disk files in asyncio applications.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitelib}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-aiofiles
Summary: File support for asyncio
Requires: python3
Provides: python3-aiofiles = %{epoch}:%{version}-%{release}
Provides: python3dist(aiofiles) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-aiofiles = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(aiofiles) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-aiofiles = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(aiofiles) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-aiofiles
aiofiles is an Apache2 licensed library, written in Python, for handling
local disk files in asyncio applications.

%files -n python%{python3_version_nodots}-aiofiles
%license LICENSE
%{python3_sitelib}/*
%endif

%if !(0%{?suse_version} > 1500)
%package -n python3-aiofiles
Summary: File support for asyncio
Requires: python3
Provides: python3-aiofiles = %{epoch}:%{version}-%{release}
Provides: python3dist(aiofiles) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-aiofiles = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(aiofiles) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-aiofiles = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(aiofiles) = %{epoch}:%{version}-%{release}

%description -n python3-aiofiles
aiofiles is an Apache2 licensed library, written in Python, for handling
local disk files in asyncio applications.

%files -n python3-aiofiles
%license LICENSE
%{python3_sitelib}/*
%endif

%changelog
