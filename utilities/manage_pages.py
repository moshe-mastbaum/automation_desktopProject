
# electron objects
from test_cases import conftest as conf
from page_objects.desktop_obj.standard_page import StandardPage

electron_task = None

class ManagePages:


    @staticmethod
    def init_desktop_pages():
        globals()['standard_cal'] = StandardPage(conf.driver)