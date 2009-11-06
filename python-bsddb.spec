%define		pname	bsddb3
Summary:	Python interface for BerkeleyDB
Summary(pl.UTF-8):	Interfejs Pythona do BerkeleyDB
Name:		python-bsddb
Version:	4.8.1
Release:	1
License:	BSD-like w/o adv. clause
Group:		Development/Languages/Python
Source0:	http://pypi.python.org/packages/source/b/bsddb3/bsddb3-%{version}.tar.gz
# Source0-md5:	d2de461ae495e70a02a64f9e2cf8982a
URL:		http://www.argo.es/~jcea/programacion/pybsddb.htm
BuildRequires:	db-devel >= 4.1.25
BuildRequires:	python-devel >= 1:2.3
%pyrequires_eq	python-modules
Obsoletes:	bsddb3
Obsoletes:	python-bsddb3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides a nearly complete wrapping of the Sleepycat C API
for the Database Environment, Database, Cursor, and Transaction
objects, and each of these is exposed as a Python Type in the
bsddb3.db module. The databse objects can use various access methods:
btree, hash, recno, and queue. For the first time all of these are
fully supported in the Python wrappers. Please see the documents in
the docs directory of the source distribution or at the website for
more details on the types and methods provided.

%description -l pl.UTF-8
Ten moduł dostarcza prawie całkowite opakowanie API C Sleepycat do
obiektów środowiska baz danych, baz danych, kursorów i transakcji, z
których każdy jest udostępniony jako pythonowy typ w module bsddb3.db.
Obiekty bazy danych mogą używać różnych metod dostępu: btree, hash,
recno i queue. Jest to pierwsza implementacja obsługi tych obiektów
dla Pythona. Więcej szczegółów o typach i metodach znajduje się w
załączonej dokumentacji lub na stronie WWW.

%prep
%setup -q -n %{pname}-%{version}

%build
env CFLAGS="%{rpmcflags}" python setup.py \
	--berkeley-db-libdir=%{_libdir} \
	--berkeley-db=%{_prefix} \
	build

%install
rm -rf $RPM_BUILD_ROOT
python -- setup.py install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2 \

# shutup check-files
rm -f $RPM_BUILD_ROOT%{py_sitedir}/bsddb3/*.py
rm -f $RPM_BUILD_ROOT%{py_sitedir}/bsddb3/tests/*.py

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.txt docs PKG-INFO
%dir %{py_incdir}/bsddb3
%dir %{py_sitedir}/bsddb3
%dir %{py_sitedir}/bsddb3/tests
%{py_incdir}/bsddb3/bsddb.h
%{py_sitedir}/bsddb3/*.py[co]
%{py_sitedir}/bsddb3/tests/*.py[co]
%attr(755,root,root) %{py_sitedir}/bsddb3/*.so
%if "%{py_ver}" > "2.4"
%{py_sitedir}/bsddb3-*.egg-info
%endif
