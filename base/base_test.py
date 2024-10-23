from new_pages.main_page import MainPage
from new_pages.admin_page import AdminPage

from pytest import fixture
class BaseTest:

     _main_page = None
     _admin_page = None

     @fixture(autouse=True)
     def setup(self, request, page):
         request.cls.page = page

     @property
     def main_page(self):
         if self._main_page is None:
             self._main_page = MainPage(self.page)
         return self._main_page

     @property
     def admin_page(self):
         if self._admin_page is None:
             self._admin_page = AdminPage(self.page)
         return self._admin_page


