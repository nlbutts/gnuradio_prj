#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Mon Mar  4 23:50:43 2019
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from PyQt4 import Qt
from gnuradio import blocks
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
import osmosdr
import sip
import sys
import time
from gnuradio import qtgui


class top_block(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Top Block")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Top Block")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Variables
        ##################################################
        self.sps = sps = 8
        self.nfilts = nfilts = 32
        self.alpha = alpha = 6.28/100.0
        self.timing_loop_bw = timing_loop_bw = 6.28/100.0
        self.samp_rate = samp_rate = 1e6
        self.rrc_taps = rrc_taps = firdes.root_raised_cosine(nfilts, 100000, sps, alpha, nfilts)
        self.rf_gain = rf_gain = 60
        self.phase_bw = phase_bw = 2*3.1415/100
        self.lpfilter = lpfilter = 10000
        self.ftune = ftune = 915e6
        self.fadj = fadj = -200000
        self.eq_gain = eq_gain = 0.01

        self.const = const = digital.constellation_bpsk().base()


        ##################################################
        # Blocks
        ##################################################
        self._timing_loop_bw_range = Range(0.0, 0.2, 0.01, 6.28/100.0, 200)
        self._timing_loop_bw_win = RangeWidget(self._timing_loop_bw_range, self.set_timing_loop_bw, 'POLY:BW', "slider", float)
        self.top_grid_layout.addWidget(self._timing_loop_bw_win, 3, 0, 1, 1)
        for r in range(3, 4):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._rf_gain_range = Range(0, 100, 10, 60, 200)
        self._rf_gain_win = RangeWidget(self._rf_gain_range, self.set_rf_gain, 'rf_gain', "counter_slider", int)
        self.top_grid_layout.addWidget(self._rf_gain_win, 2, 0, 1, 1)
        for r in range(2, 3):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._phase_bw_range = Range(0.0, 1.0, 0.01, 2*3.1415/100, 200)
        self._phase_bw_win = RangeWidget(self._phase_bw_range, self.set_phase_bw, 'Costas: BW', "counter_slider", float)
        self.top_grid_layout.addWidget(self._phase_bw_win, 1, 0, 1, 1)
        for r in range(1, 2):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._lpfilter_range = Range(0, 50000, 100, 10000, 200)
        self._lpfilter_win = RangeWidget(self._lpfilter_range, self.set_lpfilter, 'lpfilter', "counter_slider", int)
        self.top_grid_layout.addWidget(self._lpfilter_win, 1, 1, 1, 1)
        for r in range(1, 2):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(1, 2):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._ftune_range = Range(100e6, 1000e6, 1, 915e6, 200)
        self._ftune_win = RangeWidget(self._ftune_range, self.set_ftune, "ftune", "counter_slider", float)
        self.top_grid_layout.addWidget(self._ftune_win, 0, 0, 1, 1)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._fadj_range = Range(-300000, 300000, 1, -200000, 200)
        self._fadj_win = RangeWidget(self._fadj_range, self.set_fadj, "fadj", "counter_slider", float)
        self.top_grid_layout.addWidget(self._fadj_win, 0, 1, 1, 1)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(1, 2):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._eq_gain_range = Range(0.0, 0.1, 0.001, 0.01, 200)
        self._eq_gain_win = RangeWidget(self._eq_gain_range, self.set_eq_gain, 'LMS Gain', "slider", float)
        self.top_grid_layout.addWidget(self._eq_gain_win, 2, 1, 1, 1)
        for r in range(2, 3):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(1, 2):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.rtlsdr_source_0 = osmosdr.source( args="numchan=" + str(1) + " " + '' )
        self.rtlsdr_source_0.set_sample_rate(samp_rate)
        self.rtlsdr_source_0.set_center_freq(ftune, 0)
        self.rtlsdr_source_0.set_freq_corr(0, 0)
        self.rtlsdr_source_0.set_dc_offset_mode(1, 0)
        self.rtlsdr_source_0.set_iq_balance_mode(2, 0)
        self.rtlsdr_source_0.set_gain_mode(False, 0)
        self.rtlsdr_source_0.set_gain(rf_gain, 0)
        self.rtlsdr_source_0.set_if_gain(0, 0)
        self.rtlsdr_source_0.set_bb_gain(20, 0)
        self.rtlsdr_source_0.set_antenna('', 0)
        self.rtlsdr_source_0.set_bandwidth(0, 0)

        self.qtgui_time_sink_x_0 = qtgui.time_sink_f(
        	1024, #size
        	samp_rate/sps, #samp_rate
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0.enable_grid(False)
        self.qtgui_time_sink_x_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0.enable_stem_plot(False)

        if not True:
          self.qtgui_time_sink_x_0.disable_legend()

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]

        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_0_win)
        self.qtgui_sink_x_0_0_2 = qtgui.sink_c(
        	1024, #fftsize
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate/10, #bw
        	'Base band', #name
        	True, #plotfreq
        	True, #plotwaterfall
        	True, #plottime
        	True, #plotconst
        )
        self.qtgui_sink_x_0_0_2.set_update_time(1.0/10)
        self._qtgui_sink_x_0_0_2_win = sip.wrapinstance(self.qtgui_sink_x_0_0_2.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_sink_x_0_0_2_win)

        self.qtgui_sink_x_0_0_2.enable_rf_freq(False)



        self.qtgui_sink_x_0_0_1 = qtgui.sink_c(
        	1024, #fftsize
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate/10, #bw
        	'Base band', #name
        	True, #plotfreq
        	True, #plotwaterfall
        	True, #plottime
        	True, #plotconst
        )
        self.qtgui_sink_x_0_0_1.set_update_time(1.0/10)
        self._qtgui_sink_x_0_0_1_win = sip.wrapinstance(self.qtgui_sink_x_0_0_1.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_sink_x_0_0_1_win)

        self.qtgui_sink_x_0_0_1.enable_rf_freq(False)



        self.qtgui_number_sink_0_0 = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_HORIZ,
            3
        )
        self.qtgui_number_sink_0_0.set_update_time(0.10)
        self.qtgui_number_sink_0_0.set_title('error phase freq')

        labels = ['error', 'phase', 'freq', '', '',
                  '', '', '', '', '']
        units = ['', '', '', '', '',
                 '', '', '', '', '']
        colors = [("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
                  ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        for i in xrange(3):
            self.qtgui_number_sink_0_0.set_min(i, -1)
            self.qtgui_number_sink_0_0.set_max(i, 1)
            self.qtgui_number_sink_0_0.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.qtgui_number_sink_0_0.set_label(i, "Data {0}".format(i))
            else:
                self.qtgui_number_sink_0_0.set_label(i, labels[i])
            self.qtgui_number_sink_0_0.set_unit(i, units[i])
            self.qtgui_number_sink_0_0.set_factor(i, factor[i])

        self.qtgui_number_sink_0_0.enable_autoscale(False)
        self._qtgui_number_sink_0_0_win = sip.wrapinstance(self.qtgui_number_sink_0_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_number_sink_0_0_win)
        self.freq_xlating_fir_filter_xxx_0 = filter.freq_xlating_fir_filter_ccc(10, (firdes.low_pass(1, samp_rate, lpfilter, 1000)), fadj, samp_rate)
        self.digital_pfb_clock_sync_xxx_0 = digital.pfb_clock_sync_ccf(8, timing_loop_bw, (rrc_taps), nfilts, nfilts/2, 1.5, 4)
        self.digital_lms_dd_equalizer_cc_0 = digital.lms_dd_equalizer_cc(8, eq_gain, 4, const)
        self.digital_diff_decoder_bb_0 = digital.diff_decoder_bb(2)
        self.digital_costas_loop_cc_0 = digital.costas_loop_cc(phase_bw, 4, False)
        self.digital_constellation_decoder_cb_0 = digital.constellation_decoder_cb(const)
        self.blocks_uchar_to_float_0 = blocks.uchar_to_float()
        self.blocks_probe_rate_0 = blocks.probe_rate(gr.sizeof_char*1, 500.0, 0.15)
        self.blocks_message_debug_0 = blocks.message_debug()
        self.blocks_keep_one_in_n_0 = blocks.keep_one_in_n(gr.sizeof_char*1, 2)
        self._alpha_range = Range(0.0, 1, 0.01, 6.28/100.0, 200)
        self._alpha_win = RangeWidget(self._alpha_range, self.set_alpha, "alpha", "slider", float)
        self.top_grid_layout.addWidget(self._alpha_win, 3, 1, 1, 1)
        for r in range(3, 4):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(1, 2):
            self.top_grid_layout.setColumnStretch(c, 1)



        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.blocks_probe_rate_0, 'rate'), (self.blocks_message_debug_0, 'print'))
        self.connect((self.blocks_keep_one_in_n_0, 0), (self.digital_diff_decoder_bb_0, 0))
        self.connect((self.blocks_uchar_to_float_0, 0), (self.qtgui_time_sink_x_0, 0))
        self.connect((self.digital_constellation_decoder_cb_0, 0), (self.blocks_keep_one_in_n_0, 0))
        self.connect((self.digital_costas_loop_cc_0, 0), (self.digital_lms_dd_equalizer_cc_0, 0))
        self.connect((self.digital_diff_decoder_bb_0, 0), (self.blocks_probe_rate_0, 0))
        self.connect((self.digital_diff_decoder_bb_0, 0), (self.blocks_uchar_to_float_0, 0))
        self.connect((self.digital_lms_dd_equalizer_cc_0, 0), (self.digital_constellation_decoder_cb_0, 0))
        self.connect((self.digital_lms_dd_equalizer_cc_0, 0), (self.qtgui_sink_x_0_0_1, 0))
        self.connect((self.digital_pfb_clock_sync_xxx_0, 0), (self.digital_costas_loop_cc_0, 0))
        self.connect((self.digital_pfb_clock_sync_xxx_0, 1), (self.qtgui_number_sink_0_0, 0))
        self.connect((self.digital_pfb_clock_sync_xxx_0, 3), (self.qtgui_number_sink_0_0, 2))
        self.connect((self.digital_pfb_clock_sync_xxx_0, 2), (self.qtgui_number_sink_0_0, 1))
        self.connect((self.digital_pfb_clock_sync_xxx_0, 0), (self.qtgui_sink_x_0_0_2, 0))
        self.connect((self.freq_xlating_fir_filter_xxx_0, 0), (self.digital_pfb_clock_sync_xxx_0, 0))
        self.connect((self.rtlsdr_source_0, 0), (self.freq_xlating_fir_filter_xxx_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_sps(self):
        return self.sps

    def set_sps(self, sps):
        self.sps = sps
        self.set_rrc_taps(firdes.root_raised_cosine(self.nfilts, 100000, self.sps, self.alpha, self.nfilts))
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate/self.sps)

    def get_nfilts(self):
        return self.nfilts

    def set_nfilts(self, nfilts):
        self.nfilts = nfilts
        self.set_rrc_taps(firdes.root_raised_cosine(self.nfilts, 100000, self.sps, self.alpha, self.nfilts))

    def get_alpha(self):
        return self.alpha

    def set_alpha(self, alpha):
        self.alpha = alpha
        self.set_rrc_taps(firdes.root_raised_cosine(self.nfilts, 100000, self.sps, self.alpha, self.nfilts))

    def get_timing_loop_bw(self):
        return self.timing_loop_bw

    def set_timing_loop_bw(self, timing_loop_bw):
        self.timing_loop_bw = timing_loop_bw
        self.digital_pfb_clock_sync_xxx_0.set_loop_bandwidth(self.timing_loop_bw)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.rtlsdr_source_0.set_sample_rate(self.samp_rate)
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate/self.sps)
        self.qtgui_sink_x_0_0_2.set_frequency_range(0, self.samp_rate/10)
        self.qtgui_sink_x_0_0_1.set_frequency_range(0, self.samp_rate/10)
        self.freq_xlating_fir_filter_xxx_0.set_taps((firdes.low_pass(1, self.samp_rate, self.lpfilter, 1000)))

    def get_rrc_taps(self):
        return self.rrc_taps

    def set_rrc_taps(self, rrc_taps):
        self.rrc_taps = rrc_taps
        self.digital_pfb_clock_sync_xxx_0.update_taps((self.rrc_taps))

    def get_rf_gain(self):
        return self.rf_gain

    def set_rf_gain(self, rf_gain):
        self.rf_gain = rf_gain
        self.rtlsdr_source_0.set_gain(self.rf_gain, 0)

    def get_phase_bw(self):
        return self.phase_bw

    def set_phase_bw(self, phase_bw):
        self.phase_bw = phase_bw
        self.digital_costas_loop_cc_0.set_loop_bandwidth(self.phase_bw)

    def get_lpfilter(self):
        return self.lpfilter

    def set_lpfilter(self, lpfilter):
        self.lpfilter = lpfilter
        self.freq_xlating_fir_filter_xxx_0.set_taps((firdes.low_pass(1, self.samp_rate, self.lpfilter, 1000)))

    def get_ftune(self):
        return self.ftune

    def set_ftune(self, ftune):
        self.ftune = ftune
        self.rtlsdr_source_0.set_center_freq(self.ftune, 0)

    def get_fadj(self):
        return self.fadj

    def set_fadj(self, fadj):
        self.fadj = fadj
        self.freq_xlating_fir_filter_xxx_0.set_center_freq(self.fadj)

    def get_eq_gain(self):
        return self.eq_gain

    def set_eq_gain(self, eq_gain):
        self.eq_gain = eq_gain
        self.digital_lms_dd_equalizer_cc_0.set_gain(self.eq_gain)

    def get_const(self):
        return self.const

    def set_const(self, const):
        self.const = const


def main(top_block_cls=top_block, options=None):

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
