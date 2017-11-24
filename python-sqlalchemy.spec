# TODO:
# - examples and docs for python3
#   builds, but got syntax errors when buildings
#
%bcond_without	python2	# CPython 2.x module
%bcond_without	python3	# CPython 3.x module

%define		module  sqlalchemy
Summary:	Database Abstraction Library
Summary(pl.UTF-8):	Biblioteka abstrakcji baz danych
Name:		python-%{module}
Version:	1.1.15
Release:	1
License:	MIT
Group:		Libraries/Python
Source0:	https://pypi.python.org/packages/c2/f6/11fcc1ce19a7cb81b1c9377f4e27ce3813265611922e355905e57c44d164/SQLAlchemy-%{version}.tar.gz
# Source0-md5:	077f9bd3339957f53068b5572a152674
URL:		http://www.sqlalchemy.org/
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.710
%if %{with python2}
BuildRequires:	python-devel >= 1:2.4
BuildRequires:	python-distribute
BuildRequires:	python-setuptools >= 0.6-0.a9.1
%endif
%if %{with python3}
BuildRequires:	python3-2to3
BuildRequires:	python3-devel
BuildRequires:	python3-modules
%endif
%if %{with python2}
Requires:	python-modules
%endif
Provides:	python-SQLAlchemy = %{version}-%{release}
Obsoletes:	python-SQLAlchemy < 0.9.8
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Python SQL toolkit and Object Relational Mapper that gives
application developers the full power and flexibility of SQL.
SQLAlchemy provides a full suite of well known enterprise-level
persistence patterns, designed for efficient and high-performing
database access, adapted into a simple and Pythonic domain language.

Python 2.x version.

%description -l pl.UTF-8
Zestaw narzędzi SQL dla Pythona oraz odwzorowań obiektowo-relacyjnych
dających programistom całą potęgę i elastyczność SQL-a. SQLAlchemy
udostępnia pełny zbiór dobrze znanych wzorców trwałości,
zaprojektowanych do wydajnego dostępu do baz danych, zaadoptowanych do
prostej, pythonowej domeny językowej.

Wersja dla pythona 2.x.

%package -n python3-%{module}
Summary:	Database Abstraction Library
Summary(pl.UTF-8):	Biblioteka abstrakcji baz danych
Group:		Libraries/Python
Provides:	python3-SQLAlchemy = %{version}-%{release}
Obsoletes:	python3-SQLAlchemy < 0.9.8

%description -n python3-%{module}
The Python SQL toolkit and Object Relational Mapper that gives
application developers the full power and flexibility of SQL.
SQLAlchemy provides a full suite of well known enterprise-level
persistence patterns, designed for efficient and high-performing
database access, adapted into a simple and Pythonic domain language.

Python 3.x version.

%description -n python3-%{module} -l pl.UTF-8
Zestaw narzędzi SQL dla Pythona oraz odwzorowań obiektowo-relacyjnych
dających programistom całą potęgę i elastyczność SQL-a. SQLAlchemy
udostępnia pełny zbiór dobrze znanych wzorców trwałości,
zaprojektowanych do wydajnego dostępu do baz danych, zaadoptowanych do
prostej, pythonowej domeny językowej.

Wersja dla Pythona 3.x.

%prep
%setup -q -n SQLAlchemy-%{version}

%build
%if %{with python2}
CC="%{__cc}" \
CFLAGS="%{rpmcppflags} %{rpmcflags}" \
%py_build
%endif
%if %{with python3}
CC="%{__cc}" \
CFLAGS="%{rpmcppflags} %{rpmcflags}" \
%py3_build
%endif

%install
rm -rf $RPM_BUILD_ROOT
%if %{with python2}
%py_install \
	--single-version-externally-managed \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -r examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README* doc/*.html
%{py_sitedir}/sqlalchemy
%{py_sitedir}/SQLAlchemy-%{version}-py*.egg-info
%{_examplesdir}/%{name}-%{version}

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%{py3_sitedir}/sqlalchemy
%{py3_sitedir}/SQLAlchemy-%{version}-py*.egg-info
%endif
