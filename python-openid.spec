%define module openid
%define oname python3_openid

Name:		python-openid
Summary:	Python OpenID libraries
Version:	3.2.0
Release:	1
License:	Apache-2.0
Group:		Development/Python
URL:		https://github.com/necaris/python3-openid
Source0:	%{URL}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildSystem:  python
BuildArch:	noarch
BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)

# Obsolete py2 module to redirect to this python 3 module
%rename python2-openid

%description
This started out as a fork of the Python OpenID library, with changes to
make it Python 3 compatible.

It's now a port of that library, including cleanups and updates to the
code in general.

%prep -a
# Remove bundled egg-info
rm -rf %{oname}.egg-info

%files
%doc background-associations.txt README.md NEWS.md examples
%{python_sitelib}/%{module}
%{python_sitelib}/%{oname}-%{version}*.*-info
