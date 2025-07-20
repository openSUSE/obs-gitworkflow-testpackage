#
# spec file for package obs-gitworkflow-testpackage
#
# Copyright (c) 2025 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

Name:           obs-gitworkflow-testpackage
Version:	0.0.1
Release:	0
License:	GPL-3.0
Summary:	Package for testing obs-scm-bridge in open-build-service
Url:		https://github.com/openSUSE/obs-gitworkflow-testpackage.git
Group:		Productivity/Networking/Web/Utilities
Source:		%{name}-%{version}.tar.gz

%description
This package is only for testing services in open-build-service

%prep
%setup -q

%build
make

%install
make install DESTDIR=%{buildroot} %{?_smp_mflags}

%post

%postun

%files
%defattr(-,root,root)
%doc README.md

%changelog

