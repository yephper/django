from datetime import date

from django.forms import DateField, Form, SelectDateWidget
from django.test import override_settings
from django.utils import translation
from django.utils.dates import MONTHS_AP

from .base import WidgetTest


class SelectDateWidgetTest(WidgetTest):
    maxDiff = None
    widget = SelectDateWidget(
        years=('2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016'),
    )

    def test_render_empty(self):
        self.check_html(self.widget, 'mydate', '', html=(
            """
            <select name="mydate_month" id="id_mydate_month">
                <option value="0">---</option>
                <option value="1">January</option>
                <option value="2">February</option>
                <option value="3">March</option>
                <option value="4">April</option>
                <option value="5">May</option>
                <option value="6">June</option>
                <option value="7">July</option>
                <option value="8">August</option>
                <option value="9">September</option>
                <option value="10">October</option>
                <option value="11">November</option>
                <option value="12">December</option>
            </select>

            <select name="mydate_day" id="id_mydate_day">
                <option value="0">---</option>
                <option value="1">1</option>
                <option value="2">2</option>
                <option value="3">3</option>
                <option value="4">4</option>
                <option value="5">5</option>
                <option value="6">6</option>
                <option value="7">7</option>
                <option value="8">8</option>
                <option value="9">9</option>
                <option value="10">10</option>
                <option value="11">11</option>
                <option value="12">12</option>
                <option value="13">13</option>
                <option value="14">14</option>
                <option value="15">15</option>
                <option value="16">16</option>
                <option value="17">17</option>
                <option value="18">18</option>
                <option value="19">19</option>
                <option value="20">20</option>
                <option value="21">21</option>
                <option value="22">22</option>
                <option value="23">23</option>
                <option value="24">24</option>
                <option value="25">25</option>
                <option value="26">26</option>
                <option value="27">27</option>
                <option value="28">28</option>
                <option value="29">29</option>
                <option value="30">30</option>
                <option value="31">31</option>
            </select>

            <select name="mydate_year" id="id_mydate_year">
                <option value="0">---</option>
                <option value="2007">2007</option>
                <option value="2008">2008</option>
                <option value="2009">2009</option>
                <option value="2010">2010</option>
                <option value="2011">2011</option>
                <option value="2012">2012</option>
                <option value="2013">2013</option>
                <option value="2014">2014</option>
                <option value="2015">2015</option>
                <option value="2016">2016</option>
            </select>
            """
        ))

    def test_render_none(self):
        """
        Rendering the None or '' values should yield the same output.
        """
        self.assertHTMLEqual(
            self.widget.render('mydate', None),
            self.widget.render('mydate', ''),
        )

    def test_render_string(self):
        self.check_html(self.widget, 'mydate', '2010-04-15', html=(
            """
            <select name="mydate_month" id="id_mydate_month">
                <option value="0">---</option>
                <option value="1">January</option>
                <option value="2">February</option>
                <option value="3">March</option>
                <option value="4" selected="selected">April</option>
                <option value="5">May</option>
                <option value="6">June</option>
                <option value="7">July</option>
                <option value="8">August</option>
                <option value="9">September</option>
                <option value="10">October</option>
                <option value="11">November</option>
                <option value="12">December</option>
            </select>

            <select name="mydate_day" id="id_mydate_day">
                <option value="0">---</option>
                <option value="1">1</option>
                <option value="2">2</option>
                <option value="3">3</option>
                <option value="4">4</option>
                <option value="5">5</option>
                <option value="6">6</option>
                <option value="7">7</option>
                <option value="8">8</option>
                <option value="9">9</option>
                <option value="10">10</option>
                <option value="11">11</option>
                <option value="12">12</option>
                <option value="13">13</option>
                <option value="14">14</option>
                <option value="15" selected="selected">15</option>
                <option value="16">16</option>
                <option value="17">17</option>
                <option value="18">18</option>
                <option value="19">19</option>
                <option value="20">20</option>
                <option value="21">21</option>
                <option value="22">22</option>
                <option value="23">23</option>
                <option value="24">24</option>
                <option value="25">25</option>
                <option value="26">26</option>
                <option value="27">27</option>
                <option value="28">28</option>
                <option value="29">29</option>
                <option value="30">30</option>
                <option value="31">31</option>
            </select>

            <select name="mydate_year" id="id_mydate_year">
                <option value="0">---</option>
                <option value="2007">2007</option>
                <option value="2008">2008</option>
                <option value="2009">2009</option>
                <option value="2010" selected="selected">2010</option>
                <option value="2011">2011</option>
                <option value="2012">2012</option>
                <option value="2013">2013</option>
                <option value="2014">2014</option>
                <option value="2015">2015</option>
                <option value="2016">2016</option>
            </select>
            """
        ))

    def test_render_datetime(self):
        self.assertHTMLEqual(
            self.widget.render('mydate', date(2010, 4, 15)),
            self.widget.render('mydate', '2010-04-15'),
        )

    def test_render_invalid_date(self):
        """
        Invalid dates should still render the failed date.
        """
        self.check_html(self.widget, 'mydate', '2010-02-31', html=(
            """
            <select name="mydate_month" id="id_mydate_month">
                <option value="0">---</option>
                <option value="1">January</option>
                <option value="2" selected="selected">February</option>
                <option value="3">March</option>
                <option value="4">April</option>
                <option value="5">May</option>
                <option value="6">June</option>
                <option value="7">July</option>
                <option value="8">August</option>
                <option value="9">September</option>
                <option value="10">October</option>
                <option value="11">November</option>
                <option value="12">December</option>
            </select>

            <select name="mydate_day" id="id_mydate_day">
                <option value="0">---</option>
                <option value="1">1</option>
                <option value="2">2</option>
                <option value="3">3</option>
                <option value="4">4</option>
                <option value="5">5</option>
                <option value="6">6</option>
                <option value="7">7</option>
                <option value="8">8</option>
                <option value="9">9</option>
                <option value="10">10</option>
                <option value="11">11</option>
                <option value="12">12</option>
                <option value="13">13</option>
                <option value="14">14</option>
                <option value="15">15</option>
                <option value="16">16</option>
                <option value="17">17</option>
                <option value="18">18</option>
                <option value="19">19</option>
                <option value="20">20</option>
                <option value="21">21</option>
                <option value="22">22</option>
                <option value="23">23</option>
                <option value="24">24</option>
                <option value="25">25</option>
                <option value="26">26</option>
                <option value="27">27</option>
                <option value="28">28</option>
                <option value="29">29</option>
                <option value="30">30</option>
                <option value="31" selected="selected">31</option>
            </select>

            <select name="mydate_year" id="id_mydate_year">
                <option value="0">---</option>
                <option value="2007">2007</option>
                <option value="2008">2008</option>
                <option value="2009">2009</option>
                <option value="2010" selected="selected">2010</option>
                <option value="2011">2011</option>
                <option value="2012">2012</option>
                <option value="2013">2013</option>
                <option value="2014">2014</option>
                <option value="2015">2015</option>
                <option value="2016">2016</option>
            </select>
            """
        ))

    def test_custom_months(self):
        widget = SelectDateWidget(months=MONTHS_AP, years=('2013',))
        self.check_html(widget, 'mydate', '', html=(
            """
            <select name="mydate_month" id="id_mydate_month">
                <option value="0">---</option>
                <option value="1">Jan.</option>
                <option value="2">Feb.</option>
                <option value="3">March</option>
                <option value="4">April</option>
                <option value="5">May</option>
                <option value="6">June</option>
                <option value="7">July</option>
                <option value="8">Aug.</option>
                <option value="9">Sept.</option>
                <option value="10">Oct.</option>
                <option value="11">Nov.</option>
                <option value="12">Dec.</option>
            </select>

            <select name="mydate_day" id="id_mydate_day">
                <option value="0">---</option>
                <option value="1">1</option>
                <option value="2">2</option>
                <option value="3">3</option>
                <option value="4">4</option>
                <option value="5">5</option>
                <option value="6">6</option>
                <option value="7">7</option>
                <option value="8">8</option>
                <option value="9">9</option>
                <option value="10">10</option>
                <option value="11">11</option>
                <option value="12">12</option>
                <option value="13">13</option>
                <option value="14">14</option>
                <option value="15">15</option>
                <option value="16">16</option>
                <option value="17">17</option>
                <option value="18">18</option>
                <option value="19">19</option>
                <option value="20">20</option>
                <option value="21">21</option>
                <option value="22">22</option>
                <option value="23">23</option>
                <option value="24">24</option>
                <option value="25">25</option>
                <option value="26">26</option>
                <option value="27">27</option>
                <option value="28">28</option>
                <option value="29">29</option>
                <option value="30">30</option>
                <option value="31">31</option>
            </select>

            <select name="mydate_year" id="id_mydate_year">
                <option value="0">---</option>
                <option value="2013">2013</option>
            </select>
            """
        ))

    def test_selectdate_required(self):
        class GetNotRequiredDate(Form):
            mydate = DateField(widget=SelectDateWidget, required=False)

        class GetRequiredDate(Form):
            mydate = DateField(widget=SelectDateWidget, required=True)

        self.assertFalse(GetNotRequiredDate().fields['mydate'].widget.is_required)
        self.assertTrue(GetRequiredDate().fields['mydate'].widget.is_required)

    def test_selectdate_empty_label(self):
        w = SelectDateWidget(years=('2014',), empty_label='empty_label')

        # Rendering the default state with empty_label setted as string.
        self.assertInHTML('<option value="0">empty_label</option>', w.render('mydate', ''), count=3)

        w = SelectDateWidget(years=('2014',), empty_label=('empty_year', 'empty_month', 'empty_day'))

        # Rendering the default state with empty_label tuple.
        self.assertHTMLEqual(
            w.render('mydate', ''),
            """
            <select name="mydate_month" id="id_mydate_month">
                <option value="0">empty_month</option>
                <option value="1">January</option>
                <option value="2">February</option>
                <option value="3">March</option>
                <option value="4">April</option>
                <option value="5">May</option>
                <option value="6">June</option>
                <option value="7">July</option>
                <option value="8">August</option>
                <option value="9">September</option>
                <option value="10">October</option>
                <option value="11">November</option>
                <option value="12">December</option>
            </select>

            <select name="mydate_day" id="id_mydate_day">
                <option value="0">empty_day</option>
                <option value="1">1</option>
                <option value="2">2</option>
                <option value="3">3</option>
                <option value="4">4</option>
                <option value="5">5</option>
                <option value="6">6</option>
                <option value="7">7</option>
                <option value="8">8</option>
                <option value="9">9</option>
                <option value="10">10</option>
                <option value="11">11</option>
                <option value="12">12</option>
                <option value="13">13</option>
                <option value="14">14</option>
                <option value="15">15</option>
                <option value="16">16</option>
                <option value="17">17</option>
                <option value="18">18</option>
                <option value="19">19</option>
                <option value="20">20</option>
                <option value="21">21</option>
                <option value="22">22</option>
                <option value="23">23</option>
                <option value="24">24</option>
                <option value="25">25</option>
                <option value="26">26</option>
                <option value="27">27</option>
                <option value="28">28</option>
                <option value="29">29</option>
                <option value="30">30</option>
                <option value="31">31</option>
            </select>

            <select name="mydate_year" id="id_mydate_year">
                <option value="0">empty_year</option>
                <option value="2014">2014</option>
            </select>
            """,
        )

        with self.assertRaisesMessage(ValueError, 'empty_label list/tuple must have 3 elements.'):
            SelectDateWidget(years=('2014',), empty_label=('not enough', 'values'))

    @override_settings(USE_L10N=True)
    @translation.override('nl')
    def test_l10n(self):
        w = SelectDateWidget(
            years=('2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016')
        )
        self.assertEqual(
            w.value_from_datadict({'date_year': '2010', 'date_month': '8', 'date_day': '13'}, {}, 'date'),
            '13-08-2010',
        )

        self.assertHTMLEqual(
            w.render('date', '13-08-2010'),
            """
            <select name="date_day" id="id_date_day">
                <option value="0">---</option>
                <option value="1">1</option>
                <option value="2">2</option>
                <option value="3">3</option>
                <option value="4">4</option>
                <option value="5">5</option>
                <option value="6">6</option>
                <option value="7">7</option>
                <option value="8">8</option>
                <option value="9">9</option>
                <option value="10">10</option>
                <option value="11">11</option>
                <option value="12">12</option>
                <option value="13" selected="selected">13</option>
                <option value="14">14</option>
                <option value="15">15</option>
                <option value="16">16</option>
                <option value="17">17</option>
                <option value="18">18</option>
                <option value="19">19</option>
                <option value="20">20</option>
                <option value="21">21</option>
                <option value="22">22</option>
                <option value="23">23</option>
                <option value="24">24</option>
                <option value="25">25</option>
                <option value="26">26</option>
                <option value="27">27</option>
                <option value="28">28</option>
                <option value="29">29</option>
                <option value="30">30</option>
                <option value="31">31</option>
            </select>

            <select name="date_month" id="id_date_month">
                <option value="0">---</option>
                <option value="1">januari</option>
                <option value="2">februari</option>
                <option value="3">maart</option>
                <option value="4">april</option>
                <option value="5">mei</option>
                <option value="6">juni</option>
                <option value="7">juli</option>
                <option value="8" selected="selected">augustus</option>
                <option value="9">september</option>
                <option value="10">oktober</option>
                <option value="11">november</option>
                <option value="12">december</option>
            </select>

            <select name="date_year" id="id_date_year">
                <option value="0">---</option>
                <option value="2007">2007</option>
                <option value="2008">2008</option>
                <option value="2009">2009</option>
                <option value="2010" selected="selected">2010</option>
                <option value="2011">2011</option>
                <option value="2012">2012</option>
                <option value="2013">2013</option>
                <option value="2014">2014</option>
                <option value="2015">2015</option>
                <option value="2016">2016</option>
            </select>
            """,
        )

        # Even with an invalid date, the widget should reflect the entered value (#17401).
        self.assertEqual(w.render('mydate', '2010-02-30').count('selected="selected"'), 3)

        # Years before 1900 should work.
        w = SelectDateWidget(years=('1899',))
        self.assertEqual(
            w.value_from_datadict({'date_year': '1899', 'date_month': '8', 'date_day': '13'}, {}, 'date'),
            '13-08-1899',
        )
