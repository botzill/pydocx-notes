pydocx-notes
============

Overview
========
An mixin for PyDocX that export notes from textbox and wrap them into separate div

Requirements
============

* Python 2.x. 3.x
* Works on Linux, Windows, Mac OSX, BSD

Install
=======

The quick way::

    pip install pydocx_notes

Or from github repo::

    pip install https://github.com/botzill/pydocx-notes/archive/master.zip

Usage
=====

Here is an example of mixin usage:

.. code-block:: python

    from pydocx import export
    from pydocx_notes.mixin import PyDocXHTMLExporterNotesMixin


    class PyDocXHTMLExporter(PyDocXHTMLExporterNotesMixin, export.PyDocXHTMLExporter):
        pass

    docx_path = 'path/to/file/doc.docx'
    exporter = PyDocXHTMLExporter(docx_path)

    html = exporter.export()

Or you can use the same interface that pydocx is using:

.. code-block:: python

    from pydocx_notes.export import PyDocX

    html = PyDocX.to_html('path/to/docx')

Upgrading Pydocx
================
Note that when you upgrade pydocx module the mixin should work without any issues. You just need to make sure
to update pydocx and use the mixin as is. There can be cases when mixin needs to be updated if the pydocx core is
changing the same functionality that we implement as custom.
