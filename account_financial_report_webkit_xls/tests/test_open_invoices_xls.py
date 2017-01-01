# -*- coding: utf-8 -*-
# Copyright 2009-2017 Noviat.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from datetime import datetime
from .test_common_xls import TestCommonXls


class TestOpenInvoicesXls(TestCommonXls):

    def _getReportModel(self):
        return 'open.invoices.webkit'

    def _getXlsReportName(self):
        return 'account.account_report_open_invoices_xls'

    def _getBaseFilters(self):
        return {'until_date': '%s-12-31' % (datetime.now().year)}

    def test_common(self):
        common_tests = [
            x for x in dir(self)
            if callable(getattr(self, x)) and x.startswith('common_test_')]
        for test in common_tests:
            getattr(self, test)()
