# TODO:
# - examples and docs for python3
# - builds, but got syntax errors when buildings
#
%bcond_without	python3
%bcond_without	python2
%define		module  SQLAlchemy
#
Summary:	Database Abstraction Library
Summary(pl.UTF-8):	Biblioteka abstrakcji baz danych
Name:		python-%{module}
Version:	0.6.3
Release:	0.1
License:	MIT
Group:		Libraries/Python
Source0:	http://downloads.sourceforge.net/sqlalchemy/%{module}-%{version}.tar.gz
# Source0-md5:	103bdc156a95291a302acc42c136bf7d
URL:		http://www.sqlalchemy.org/
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
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
%if %{with python2}
%pyrequires_eq  python-modules
%endif
BuildArch:	noarch
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
%setup -q -n %{module}-%{version}

%build
%if %{with python2}
%{__python} setup.py build -b build-2
%endif
%if %{with python3}
%{__python3} setup.py build -b build-3
%endif

%install
rm -rf $RPM_BUILD_ROOT
%if %{with python2}
%{__python} setup.py build -b build-2 \
	install \
	--single-version-externally-managed \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_postclean
%endif

%if %{with python3}
%{__python3} setup.py build -b build-3 \
	install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

%py3_postclean
%endif

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -r examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README* doc/*.html
%{py_sitescriptdir}/SQLAlchemy*
%{py_sitescriptdir}/sqlalchemy*
%{_examplesdir}/%{name}-%{version}

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%{py3_sitescriptdir}/SQLAlchemy*
%{py3_sitescriptdir}/sqlalchemy*
%endif
