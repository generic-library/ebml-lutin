#!/usr/bin/python
import realog.debug as debug
import lutin.tools as tools


def get_type():
	return "LIBRARY"

def get_desc():
	return "ebml library"

def get_licence():
	return "LGPL-2.1"

def get_maintainer():
	return ["Moritz Bunkus <moritz@bunkus.org>"]

def get_version():
	return [1,3,4]

def configure(target, my_module):
	my_module.add_src_file([
	    'ebml/src/EbmlHead.cpp',
	    'ebml/src/EbmlCrc32.cpp',
	    'ebml/src/EbmlString.cpp',
	    'ebml/src/MemIOCallback.cpp',
	    'ebml/src/EbmlBinary.cpp',
	    'ebml/src/EbmlStream.cpp',
	    'ebml/src/EbmlSubHead.cpp',
	    'ebml/src/EbmlFloat.cpp',
	    'ebml/src/EbmlVersion.cpp',
	    'ebml/src/MemReadIOCallback.cpp',
	    'ebml/src/EbmlDate.cpp',
	    'ebml/src/IOCallback.cpp',
	    'ebml/src/Debug.cpp',
	    'ebml/src/EbmlUInteger.cpp',
	    'ebml/src/EbmlVoid.cpp',
	    'ebml/src/EbmlSInteger.cpp',
	    'ebml/src/EbmlContexts.cpp',
	    'ebml/src/EbmlDummy.cpp',
	    'ebml/src/StdIOCallback.cpp',
	    'ebml/src/EbmlUnicodeString.cpp',
	    'ebml/src/SafeReadIOCallback.cpp',
	    'ebml/src/EbmlMaster.cpp',
	    'ebml/src/EbmlElement.cpp',
	    ])
	my_module.add_header_file([
	    'ebml/ebml/EbmlMaster.h',
	    'ebml/ebml/EbmlHead.h',
	    'ebml/ebml/EbmlBinary.h',
	    'ebml/ebml/EbmlSubHead.h',
	    'ebml/ebml/EbmlString.h',
	    'ebml/ebml/IOCallback.h',
	    'ebml/ebml/EbmlStream.h',
	    'ebml/ebml/EbmlDate.h',
	    'ebml/ebml/EbmlContexts.h',
	    'ebml/ebml/EbmlEndian.h',
	    'ebml/ebml/Debug.h',
	    'ebml/ebml/EbmlCrc32.h',
	    'ebml/ebml/EbmlTypes.h',
	    'ebml/ebml/EbmlUnicodeString.h',
	    'ebml/ebml/MemReadIOCallback.h',
	    'ebml/ebml/EbmlConfig.h',
	    'ebml/ebml/EbmlFloat.h',
	    'ebml/ebml/MemIOCallback.h',
	    'ebml/ebml/EbmlSInteger.h',
	    'ebml/ebml/EbmlElement.h',
	    'ebml/ebml/EbmlDummy.h',
	    'ebml/ebml/StdIOCallback.h',
	    'ebml/ebml/EbmlUInteger.h',
	    'ebml/ebml/EbmlVoid.h',
	    'ebml/ebml/EbmlId.h',
	    'ebml/ebml/SafeReadIOCallback.h',
	    'ebml/ebml/EbmlVersion.h',
	    ],
	    destination_path="ebml")
	my_module.add_header_file([
	    'ebml/ebml/c/libebml_t.h',
	    ],
	    destination_path="ebml/c")
	my_module.add_depend([
	    'cxx',
	    'pthread'
	    ])
	my_module.compile_version("C++", 2003)
	return True


