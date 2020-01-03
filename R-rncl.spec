#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-rncl
Version  : 0.8.3
Release  : 19
URL      : https://cran.r-project.org/src/contrib/rncl_0.8.3.tar.gz
Source0  : https://cran.r-project.org/src/contrib/rncl_0.8.3.tar.gz
Summary  : An Interface to the Nexus Class Library
Group    : Development/Tools
License  : BSD-2-Clause
Requires: R-rncl-lib = %{version}-%{release}
Requires: R-Rcpp
Requires: R-progress
BuildRequires : R-Rcpp
BuildRequires : R-progress
BuildRequires : buildreq-R
BuildRequires : util-linux

%description
---
title: An R interface to the NEXUS Class Library
---
[![Build Status](https://travis-ci.org/fmichonneau/rncl.svg)](https://travis-ci.org/fmichonneau/rncl)
[![Build status](https://ci.appveyor.com/api/projects/status/bfcjqt83esp0nnak)](https://ci.appveyor.com/project/fmichonneau/rncl)
[![Coverage Status](https://coveralls.io/repos/fmichonneau/rncl/badge.svg)](https://coveralls.io/r/fmichonneau/rncl)
[![Research software impact](http://depsy.org/api/package/cran/rncl/badge.svg)](http://depsy.org/package/r/rncl)

%package lib
Summary: lib components for the R-rncl package.
Group: Libraries

%description lib
lib components for the R-rncl package.


%prep
%setup -q -c -n rncl

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1571894048

%install
export SOURCE_DATE_EPOCH=1571894048
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library rncl
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library rncl
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library rncl
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc rncl || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/rncl/DESCRIPTION
/usr/lib64/R/library/rncl/INDEX
/usr/lib64/R/library/rncl/LICENSE
/usr/lib64/R/library/rncl/Meta/Rd.rds
/usr/lib64/R/library/rncl/Meta/features.rds
/usr/lib64/R/library/rncl/Meta/hsearch.rds
/usr/lib64/R/library/rncl/Meta/links.rds
/usr/lib64/R/library/rncl/Meta/nsInfo.rds
/usr/lib64/R/library/rncl/Meta/package.rds
/usr/lib64/R/library/rncl/NAMESPACE
/usr/lib64/R/library/rncl/NEWS.md
/usr/lib64/R/library/rncl/R/rncl
/usr/lib64/R/library/rncl/R/rncl.rdb
/usr/lib64/R/library/rncl/R/rncl.rdx
/usr/lib64/R/library/rncl/help/AnIndex
/usr/lib64/R/library/rncl/help/aliases.rds
/usr/lib64/R/library/rncl/help/paths.rds
/usr/lib64/R/library/rncl/help/rncl.rdb
/usr/lib64/R/library/rncl/help/rncl.rdx
/usr/lib64/R/library/rncl/html/00Index.html
/usr/lib64/R/library/rncl/html/R.css
/usr/lib64/R/library/rncl/newick_bad/Gudrun.nex
/usr/lib64/R/library/rncl/newick_bad/bad_newick.tre
/usr/lib64/R/library/rncl/newick_good/Gudrun.tre
/usr/lib64/R/library/rncl/newick_good/missing_edge_lengths.tre
/usr/lib64/R/library/rncl/newick_good/simpleTree.tre
/usr/lib64/R/library/rncl/newick_good/singleton_tree.tre
/usr/lib64/R/library/rncl/newick_good/singleton_with_edge_length.tre
/usr/lib64/R/library/rncl/newick_good/test_sing.tre
/usr/lib64/R/library/rncl/newick_good/tree1.tre
/usr/lib64/R/library/rncl/newick_good/tree2.tre
/usr/lib64/R/library/rncl/nexusfiles/MultiLineTrees.nex
/usr/lib64/R/library/rncl/nexusfiles/badnex.nex
/usr/lib64/R/library/rncl/nexusfiles/co1.nex
/usr/lib64/R/library/rncl/nexusfiles/multiLines.rds
/usr/lib64/R/library/rncl/nexusfiles/newick.tre
/usr/lib64/R/library/rncl/nexusfiles/test_empty.nex
/usr/lib64/R/library/rncl/nexusfiles/test_subset_alltaxa.nex
/usr/lib64/R/library/rncl/nexusfiles/test_subset_taxa.nex
/usr/lib64/R/library/rncl/nexusfiles/test_underscores.nex
/usr/lib64/R/library/rncl/nexusfiles/treeWithDiscreteData.nex
/usr/lib64/R/library/rncl/nexusfiles/treeWithUnderscoreLabels.nex
/usr/lib64/R/library/rncl/tests/test-all.R
/usr/lib64/R/library/rncl/tests/testthat/test.badnex.R
/usr/lib64/R/library/rncl/tests/testthat/test.rncl.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/rncl/libs/rncl.so
/usr/lib64/R/library/rncl/libs/rncl.so.avx2
/usr/lib64/R/library/rncl/libs/rncl.so.avx512
