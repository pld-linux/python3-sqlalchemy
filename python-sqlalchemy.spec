#
# Conditional build:
%bcond_without	python2	# CPython 2.x module
%bcond_without	python3	# CPython 3.x module
%bcond_without	tests	# unit tests

%define		module  sqlalchemy
Summary:	Database Abstraction Library for Python 2
Summary(pl.UTF-8):	Biblioteka abstrakcji baz danych dla Pythona 2
Name:		python-%{module}
# keep 1.x here for python2 support
Version:	1.4.50
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/sqlalchemy/
Source0:	https://files.pythonhosted.org/packages/source/S/SQLAlchemy/SQLAlchemy-%{version}.tar.gz
# Source0-md5:	0796f9734d5898945d7802ad00ac1723
Patch0:		%{name}-tests.patch
URL:		https://www.sqlalchemy.org/
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-devel >= 1:2.7
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools >= 0.6-0.a9.1
%if %{with tests}
BuildRequires:	python-mock
BuildRequires:	python-pytest >= 4.6.11
BuildRequires:	python-pytest-xdist
%endif
%endif
%if %{with python3}
BuildRequires:	python3-devel >= 1:3.4
BuildRequires:	python3-modules >= 1:3.4
BuildRequires:	python3-setuptools >= 0.6-0.a9.1
%if %{with tests}
BuildRequires:	python3-pytest >= 6.2
BuildRequires:	python3-pytest-xdist
%endif
%endif
Requires:	python-modules
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
Zestaw narzędzi SQL oraz odwzorowań obiektowo-relacyjnych dla Pythona,
dający programistom całą potęgę i elastyczność SQL-a. SQLAlchemy
udostępnia pełny zbiór dobrze znanych wzorców trwałości,
zaprojektowanych z myślą o efektywny i wydajnym dostępem do baz
danych, zaadaptowanych do prostego, pythonowego języka.

Wersja dla pythona 2.x.

%package -n python3-%{module}
Summary:	Database Abstraction Library for Python 3
Summary(pl.UTF-8):	Biblioteka abstrakcji baz danych dla Pythona 3
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
Zestaw narzędzi SQL oraz odwzorowań obiektowo-relacyjnych dla Pythona,
dający programistom całą potęgę i elastyczność SQL-a. SQLAlchemy
udostępnia pełny zbiór dobrze znanych wzorców trwałości,
zaprojektowanych z myślą o efektywny i wydajnym dostępem do baz
danych, zaadaptowanych do prostego, pythonowego języka.

Wersja dla Pythona 3.x.

%package apidocs
Summary:	API documentation for Python SQLAlchemy module
Summary(pl.UTF-8):	Dokumentacja API modułu Pythona SQLAlchemy
Group:		Documentation
BuildArch:	noarch

%description apidocs
API documentation for Python SQLAlchemy module.

%description apidocs -l pl.UTF-8
Dokumentacja API modułu Pythona SQLAlchemy.

%package examples
Summary:	Examples for Python SQLAlchemy module
Summary(pl.UTF-8):	Przykłady do modułu Pythona SQLAlchemy
Group:		Documentation
BuildArch:	noarch

%description examples
Examples for Python SQLAlchemy module.

%description examples -l pl.UTF-8
Przykłady do modułu Pythona SQLAlchemy.

%prep
%setup -q -n SQLAlchemy-%{version}
%patch0 -p1

%build
%if %{with python2}
%py_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
PYTHONPATH=$(echo $(pwd)/build-2/lib.linux-*) \
%{__python} -m pytest test -k 'not test_fixture_five'
# in OverlappingFksSiblingTest.test_fixture_five[False] reported warnings differ from reference
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
PYTHONPATH=$(echo $(pwd)/build-3/lib.linux-*) \
%{__python3} -m pytest test
%endif
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -pr examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS CHANGES LICENSE README.rst
%dir %{py_sitedir}/sqlalchemy
%{py_sitedir}/sqlalchemy/connectors
%{py_sitedir}/sqlalchemy/databases
%{py_sitedir}/sqlalchemy/dialects
%{py_sitedir}/sqlalchemy/engine
%{py_sitedir}/sqlalchemy/event
%{py_sitedir}/sqlalchemy/ext
%{py_sitedir}/sqlalchemy/future
%{py_sitedir}/sqlalchemy/orm
%{py_sitedir}/sqlalchemy/pool
%{py_sitedir}/sqlalchemy/sql
%{py_sitedir}/sqlalchemy/testing
%{py_sitedir}/sqlalchemy/util
%attr(755,root,root) %{py_sitedir}/sqlalchemy/cimmutabledict.so
%attr(755,root,root) %{py_sitedir}/sqlalchemy/cprocessors.so
%attr(755,root,root) %{py_sitedir}/sqlalchemy/cresultproxy.so
%{py_sitedir}/sqlalchemy/*.py[co]
%{py_sitedir}/SQLAlchemy-%{version}-py*.egg-info

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc AUTHORS CHANGES LICENSE README.rst
%dir %{py3_sitedir}/sqlalchemy
%{py3_sitedir}/sqlalchemy/connectors
%{py3_sitedir}/sqlalchemy/databases
%{py3_sitedir}/sqlalchemy/dialects
%{py3_sitedir}/sqlalchemy/engine
%{py3_sitedir}/sqlalchemy/event
%{py3_sitedir}/sqlalchemy/ext
%{py3_sitedir}/sqlalchemy/future
%{py3_sitedir}/sqlalchemy/orm
%{py3_sitedir}/sqlalchemy/pool
%{py3_sitedir}/sqlalchemy/sql
%{py3_sitedir}/sqlalchemy/testing
%{py3_sitedir}/sqlalchemy/util
%attr(755,root,root) %{py3_sitedir}/sqlalchemy/cimmutabledict.cpython-*.so
%attr(755,root,root) %{py3_sitedir}/sqlalchemy/cprocessors.cpython-*.so
%attr(755,root,root) %{py3_sitedir}/sqlalchemy/cresultproxy.cpython-*.so
%{py3_sitedir}/sqlalchemy/*.py
%{py3_sitedir}/sqlalchemy/__pycache__
%{py3_sitedir}/SQLAlchemy-%{version}-py*.egg-info
%endif

%files apidocs
%defattr(644,root,root,755)
%doc doc/{_images,_modules,_static,changelog,core,dialects,faq,orm,*.html,*.js}

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
