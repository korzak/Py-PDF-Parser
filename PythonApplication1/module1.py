#diff -Naur a/slate.py b/slate.py
#--- a/slate.py	2017-05-28 14:00:00.000000000 +0800
#+++ b/slate.py	2017-05-28 14:30:00.000000000 +0800
#@@ -1,6 +1,9 @@
 from StringIO import StringIO

-from pdfminer.pdfparser import PDFParser, PDFDocument
+#from pdfminer.pdfparser import PDFParser, PDFDocument
+from pdfminer.pdfparser import PDFParser
+from pdfminer.pdfdocument import PDFDocument
+from pdfminer.pdfpage import PDFPage
 from pdfminer.pdfinterp import PDFResourceManager
 from pdfminer.pdfinterp import PDFPageInterpreter as PI
 from pdfminer.pdfdevice import PDFDevice
#@@ -12,8 +15,8 @@

 class PDFPageInterpreter(PI):
     def process_page(self, page):
-        if 1 <= self.debug:
-            print >>stderr, 'Processing page: %r' % page
+        #if 1 <= self.debug:
+        #    print >>stderr, 'Processing page: %r' % page
         (x0,y0,x1,y1) = page.mediabox
         if page.rotate == 90:
             ctm = (0,-1,1,0, -y0,x1)
#@@ -33,16 +36,18 @@
 class PDF(list):
     def __init__(self, file, password='', just_text=1):
         self.parser = PDFParser(file)
-        self.doc = PDFDocument()
+        #self.doc = PDFDocument()
+        self.doc = PDFDocument(self.parser, password)
         self.parser.set_document(self.doc)
-        self.doc.set_parser(self.parser)
-        self.doc.initialize(password)
+        #self.doc.set_parser(self.parser)
+        #self.doc.initialize(password)
         if self.doc.is_extractable:
             self.resmgr = PDFResourceManager()
             self.device = TextConverter(self.resmgr, outfp=StringIO())
             self.interpreter = PDFPageInterpreter(
                self.resmgr, self.device)
-            for page in self.doc.get_pages():
+            #for page in self.doc.get_pages():
+            for page in PDFPage.create_pages(self.doc):
                 self.append(self.interpreter.process_page(page))
             self.metadata = self.doc.info
         if just_text:
