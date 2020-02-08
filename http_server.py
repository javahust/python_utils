from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import cgi
import sys
import traceback

feature_result = '{"usd_txn_fp_6hr":"0.1","cnt_esc_inr_360d":"0.1","rt_3pty_usd_30d":"0.1","cnt_txn_fp_12hr":"0.1",' \
                 '"avg_st_dsr_360d":"0.1","avg_ck2scan_days_5d_90d":"0.1","avg_com_dsr_360d":"0.1",' \
                 '"usd_esc_inr_90d":"0.1","usd_iph_lstg_1hr":"0.1","usd_txn_fp_1d":"0.1","avg_st_dsr_180d":"0.1",' \
                 '"usd_iph_lstg_12hr":"0.1","usd_mbl_lstg_1hr":"0.1","usd_opened_inr_30d":"0.1",' \
                 '"usd_txn_elec_fp_1hr":"0.1","usd_opened_inr_90d":"0.1","cnt_ip_slr_cntry_match_30d":"0.1",' \
                 '"usd_txn_elec_fp_1d":"0.1","selling_age_days":"0.1","cnt_esc_clm_180d":"0.1","last_lmt_qty":"0.1",' \
                 '"rt_usd_shp_trk_5d_90d":"0.1","ucnt_lstg_ip2_30d":"0.1","cnt_ipitemcntry_match_30d":"0.1",' \
                 '"usd_iph_lstg_6hr":"0.1","rt_3pty_lstg_12hr":"0.1","rt_3pty_lstg_30d":"0.1",' \
                 '"usd_esc_inr_360d":"0.1","cnt_slr_pstv_fdbk_360d":"0.1","usd_opened_snad_360d":"0.1",' \
                 '"rt_msg_rcvd_no_rspns_7d":"0.1","avg_ck2scan_days_5d_180d":"0.1","cnt_opened_inr_360d":"0.1",' \
                 '"usd_opened_inr_180d":"0.1","rt_usd_shp_trk_5d_14d":"0.1","rt_loc_mismatch_lstg_14d":"0.1",' \
                 '"rt_usd_shp_no_cfszip_5d_14d":"0.1","cnt_msg_rcvd_no_rspns_7d":"0.1","pct_cnt_txn_elec_60d":"0.1",' \
                 '"rt_cnt_shp_trk_5d_90d":"0.1","cnt_ipitemcntry_match_14d":"0.1",' \
                 '"rt_cnt_shp_no_cfszip_5d_30d":"0.1","cnt_opened_snad_1d":"0.1","hist_d21_clm_elgbl_amt":"0.1",' \
                 '"avg_ck2scan_days_5d_60d":"0.1","rt_c2cblt_usd_30d":"0.1","last_lmt_chng_days":"0.1",' \
                 '"rt_cnt_shp_trk_5d_60d":"0.1","lstg_photo_cnt_rt_30d":"0.1","usd_txn_fp_1hr":"0.1",' \
                 '"cnt_opened_clm_360d":"0.1","rt_cnt_shp_trk_5d_30d":"0.1","lstg_ttl_usd_1d":"0.1",' \
                 '"usd_opened_snad_7d":"0.1","frst_lmt_gmv_90d":"0.1","hist_d30_clm_elgbl_amt":"0.1",' \
                 '"cnt_c2cblt_lstg_30d":"0.1","cnt_mbl_lstg_1d":"0.1","usd_shp_ups_5d_30d":"0.1",' \
                 '"usd_txn_elec_60d":"0.1","cnt_slr_pstv_fdbk_180d":"0.1","cnt_opened_inr_7d":"0.1",' \
                 '"rt_usd_shp_no_cfszip_5d_7d":"0.1","usd_esc_clm_30d":"0.1","usd_opened_snad_30d":"0.1",' \
                 '"rt_usd_shp_trk_5d_30d":"0.1","rt_usd_shp_trk_5d_7d":"0.1","cnt_txn_30d":"0.1",' \
                 '"usd_loss_pre_recoupment_60d_360d":"0.1","cnt_shp_usps_5d_7d":"0.1",' \
                 '"rt_ip_slr_cntry_match_12hr":"0.1","rt_usd_shp_no_acpt_5d_90d":"0.1",' \
                 '"cnt_ip_slr_cntry_match_14d":"0.1","lstg_photo_usd_30min":"0.1","usd_esc_clm_90d":"0.1",' \
                 '"rt_usd_shp_no_acpt_5d_14d":"0.1","usd_txn_fp_30min":"0.1","rt_ipitemcntry_match_12hr":"0.1",' \
                 '"cnt_ipitemzip_match_7d":"0.1","cnt_txn_fp_7d":"0.1","usd_3pty_lstg_7d":"0.1",' \
                 '"avg_ck2scan_days_5d_7d":"0.1","cnt_mbl_lstg_14d":"0.1","cnt_esc_clm_14d":"0.1",' \
                 '"usd_loss_pre_recoupment_60d_180d":"0.1","usd_iph_lstg_1d":"0.1","rt_msg_rcvd_no_rspns_30d":"0.1",' \
                 '"usd_opened_inr_360d":"0.1","usd_fvf_shp_fee_90d":"0.1","rt_msg_rcvd_no_rspns_14d":"0.1",' \
                 '"lstg_photo_cnt_rt_14d":"0.1","usd_txn_elec_auc_60d":"0.1","cnt_slr_pstv_fdbk_14d":"0.1",' \
                 '"cnt_ipitemzip_match_14d":"0.1","cnt_txn_180d":"0.1","rt_ucnt_itemzip_2d_30d":"0.1",' \
                 '"rt_cnt_shp_label_5d_30d":"0.1","ratio_pct_cnt_txn_med_1d_90d":"0.1","usd_txn_fp_7d":"0.1",' \
                 '"cnt_iph_lstg_1d":"0.1","avg_usd_txn_7d":"0.1","rt_c2cblt_lstg_30d":"0.1",' \
                 '"rt_ipitemcntry_match_1hr":"0.1","cnt_c2cblt_lstg_7d":"0.1","cnt_userid_chng_90d":"0.1",' \
                 '"pct_cnt_txn_clct_7d":"0.1","rt_cnt_shp_no_acpt_5d_7d":"0.1","hist_d7_clm_elgbl_amt":"0.1",' \
                 '"usd_fvf_shp_fee_1d":"0.1","usd_txn_elec_14d":"0.1","cnt_slr_tot_fdbk_360d":"0.1",' \
                 '"rt_cnt_shp_usps_5d_30d":"0.1","usd_opened_clm_180d":"0.1","usd_txn_elec_7d":"0.1",' \
                 '"usd_fvf_crd_30d":"0.1","usd_loss_pre_recoupment_60d_90d":"0.1","cnt_days_last_cntry_chng":"0.1",' \
                 '"cnt_slr_tot_fdbk_90d":"0.1","cnt_txn_pa_auc_90d":"0.1","usd_opened_snad_1d":"0.1",' \
                 '"cnt_3pty_lstg_14d":"0.1","pct_cnt_txn_hg_1d":"0.1","rt_auc_1d_3d_lstg_12hr":"0.1",' \
                 '"cnt_opened_inr_1d":"0.1","usd_esc_clm_180d":"0.1","lstg_bold_usd_rt_7d":"0.1",' \
                 '"cnt_msg_rcvd_no_rspns_1d":"0.1","usd_opened_inr_1d":"0.1","cnt_txn_14d":"0.1",' \
                 '"frst_lmt_gmv_30d":"0.1","rt_ucnt_itemzip_22d_30d":"0.1","usd_opened_clm_360d":"0.1",' \
                 '"cnt_txn_360d":"0.1","usd_txn_hg_fp_12hr":"0.1","usd_shp_trk_10d_90d":"0.1",' \
                 '"ucnt_lstg_stcntry_2d_30d":"0.1","avg_msg_rspns_len_30d":"0.1","avg_ck2ship_days_5d_30d":"0.1",' \
                 '"rt_site_mismatch_lstg_12hr":"0.1","usd_shp_label_5d_7d":"0.1","rt_cnt_shp_web_5d_7d":"0.1",' \
                 '"lstg_gen_ttl_cnt_14d":"0.1","usd_opened_clm_60d":"0.1","rt_iph_usd_30d":"0.1",' \
                 '"avg_ck2ship_days_5d_60d":"0.1","usd_txn_14d":"0.1","cnt_opened_clm_12hr":"0.1",' \
                 '"lstg_gen_ttl_cnt_30d":"0.1","cnt_msg_rcvd_no_rspns_14d":"0.1","avg_ck2scan_days_5d_14d":"0.1",' \
                 '"rt_ipitemcntry_match_6hr":"0.1","usd_esc_clm_360d":"0.1","rt_cnt_shp_label_5d_14d":"0.1",' \
                 '"rt_usd_shp_no_acpt_5d_7d":"0.1","cnt_ipitemcntry_match_7d":"0.1","avg_dly_userid_chng_90d":"0.1",' \
                 '"cnt_txn_ttl_5d_14d":"0.1","rt_cnt_shp_pbi_5d_60d":"0.1","usd_ttl_lstg_12hr":"0.1",' \
                 '"usd_shp_trk_10d_180d":"0.1","rt_usd_shp_no_ship_5d_30d":"0.1","lstg_gen_ttl_usd_1hr":"0.1",' \
                 '"cnt_shp_usps_5d_180d":"0.1","cnt_shp_trk_5d_180d":"0.1","avg_rspns_hrs_30d":"0.1",' \
                 '"rt_alt_shp_type_lstg_7d":"0.1","usd_opened_snad_90d":"0.1",' \
                 '"ratio_pct_cnt_txn_elec_14d_360d":"0.1","usd_c2cblt_lstg_1d":"0.1","usd_slr_credit_7d":"0.1",' \
                 '"avg_st_dsr_60d":"0.1","cnt_shp_trk_5d_14d":"0.1","cnt_alt_shp_type_lstg_30d":"0.1",' \
                 '"usd_c2cblt_lstg_14d":"0.1","cnt_shp_trk_5d_30d":"0.1","usd_txn_med_1hr":"0.1",' \
                 '"usd_shp_label_5d_180d":"0.1","cnt_iph_lstg_7d":"0.1","cnt_ipitemzip_match_30d":"0.1",' \
                 '"usd_txn_pa_auc_7d":"0.1","rt_alt_shp_type_usd_14d":"0.1","cnt_esc_inr_90d":"0.1",' \
                 '"usd_auc_le3d_lstg_30d":"0.1","frst_lmt_gmv_14d":"0.1","rt_cnt_shp_no_acpt_5d_30d":"0.1",' \
                 '"cnt_txn_fash_60d":"0.1","rt_auc_le3d_usd_30d":"0.1","pct_cnt_txn_elec_7d":"0.1",' \
                 '"pct_cnt_txn_hg_7d":"0.1","ucnt_lstg_cntry_30d":"0.1","rt_auc_le3d_lstg_14d":"0.1",' \
                 '"avg_lstgcnt_itemzip_14d":"0.1","lstg_arc_cnt_rt_14d":"0.1","usd_alt_shp_type_lstg_12hr":"0.1",' \
                 '"cnt_opened_clm_1d":"0.1","lstg_photo_cnt_rt_1d":"0.1","rt_adrd_lstg_7d":"0.1",' \
                 '"cnt_loc_mismatch_lstg_30d":"0.1","rt_usd_shp_web_5d_7d":"0.1","last_lmt_gmv":"0.1",' \
                 '"rt_cnt_shp_trk_5d_14d":"0.1","usd_txn_med_auc_1hr":"0.1","cnt_opened_inr_14d":"0.1",' \
                 '"rt_auc_le3d_lstg_30d":"0.1","lstg_photo_usd_rt_1d":"0.1","avg_iad_dsr_6hr":"0.1",' \
                 '"cnt_txn_elec_fp_30min":"0.1","rt_ucnt_itemzip_8d_30d":"0.1","usd_adrd_lstg_7d":"0.1",' \
                 '"cnt_msg_rcvd_no_rspns_30d":"0.1","usd_alt_shp_type_lstg_7d":"0.1","ucnt_lstg_cntry_7d":"0.1",' \
                 '"usd_txn_fp_360d":"0.1","usd_txn_fash_30d":"0.1","hist_d14_clm_elgbl_amt":"0.1",' \
                 '"usd_txn_hg_fp_1d":"0.1","ucnt_lstg_ip1_7d":"0.1","cnt_lmt_chng_rec_14d":"0.1",' \
                 '"usd_fvf_fee_14d":"0.1","cnt_shp_fedex_5d_60d":"0.1","cnt_pwd_chng_90d":"0.1",' \
                 '"usd_txn_pa_fp_60d":"0.1","cnt_opened_snad_90d":"0.1","cnt_esc_inr_30d":"0.1",' \
                 '"cnt_msg_rcvd_7d":"0.1","rt_loc_mismatch_lstg_1d":"0.1","rt_usd_shp_no_acpt_5d_180d":"0.1",' \
                 '"cnt_c2cblt_lstg_14d":"0.1","rt_cnt_shp_fedex_5d_30d":"0.1","avg_dly_pwdhnt_chng_90d":"0.1",' \
                 '"avg_com_dsr_30d":"0.1","usd_txn_clct_fp_360d":"0.1","rt_auc_le3d_lstg_7d":"0.1",' \
                 '"usd_slr_fee_7d":"0.1","cnt_txn_7d":"0.1","cnt_txn_elec_auc_90d":"0.1","usd_txn_7d":"0.1",' \
                 '"cnt_esc_clm_30d":"0.1","usd_txn_clct_90d":"0.1","ucnt_lstg_itemzip_7d":"0.1",' \
                 '"rt_cnt_shp_weblpp_5d_180d":"0.1","usd_slr_net_fee_30d":"0.1","rt_alt_shp_opt_lstg_14d":"0.1",' \
                 '"usd_fvf_fee_7d":"0.1","rt_lmt_qty_chng_90d":"0.1","rt_adrd_usd_30d":"0.1",' \
                 '"usd_3pty_lstg_30d":"0.1","lstg_gen_sco_cnt_rt_30d":"0.1","cnt_3pty_lstg_7d":"0.1",' \
                 '"rt_ucnt_stcntry_2d_30d":"0.1","cnt_txn_ttl_5d_30d":"0.1","lstg_gen_ttl_usd_5min":"0.1",' \
                 '"cnt_3pty_lstg_30d":"0.1","lstg_gen_ss_usd_14d":"0.1","rt_usd_shp_no_acpt_5d_60d":"0.1",' \
                 '"lstg_photo_usd_rt_30d":"0.1","ratio_pct_cnt_txn_bi_14d_90d":"0.1",' \
                 '"cnt_days_last_userid_chng":"0.1","lmt_gmv_chng_60d":"0.1","pct_cnt_txn_fash_1d":"0.1",' \
                 '"ratio_asp_7d_180d":"0.1","rt_alt_shp_type_usd_30d":"0.1","usd_opened_inr_12hr":"0.1",' \
                 '"usd_shp_upld_web_5d_7d":"0.1","cnt_slr_ngtv_fdbk_360d":"0.1",' \
                 '"ratio_pct_cnt_txn_fash_7d_180d":"0.1","usd_txn_auc_5min":"0.1","rt_auc_le3d_lstg_1hr":"0.1",' \
                 '"ucnt_lstg_itemzip_30d":"0.1","cnt_shp_trk_5d_7d":"0.1","usd_txn_med_auc_7d":"0.1",' \
                 '"cnt_shp_upld_unkn_5d_30d":"0.1","usd_slr_fee_60d":"0.1","avg_iad_dsr_30d":"0.1",' \
                 '"ucnt_info_chng_type_30min":"0.1","cnt_shp_trk_no_cfszip_5d_30d":"0.1",' \
                 '"rt_usd_shp_no_dlvr_10d_30d":"0.1","cnt_txn_bi_7d":"0.1","usd_slr_fee_14d":"0.1",' \
                 '"avg_ship2scan_days_5d_60d":"0.1","usd_ttl_lstg_30d":"0.1","avg_msg_rcvd_len_14d":"0.1",' \
                 '"ratio_pct_cnt_txn_bi_1d_7d":"0.1","usd_fvf_shp_fee_30d":"0.1","cnt_days_last_info_chng":"0.1",' \
                 '"cnt_txn_hg_fp_180d":"0.1","cnt_opened_snad_14d":"0.1","usd_slr_fee_90d":"0.1",' \
                 '"usd_shp_label_5d_90d":"0.1","cnt_ttl_lstg_30d":"0.1","rt_auc_1d_3d_lstg_30d":"0.1",' \
                 '"pct_cnt_txn_elec_180d":"0.1","usd_ad_net_fee_90d":"0.1","avg_usd_txn_30d":"0.1",' \
                 '"cnt_cntry_id_chng_1d":"0.1","usd_txn_bi_12hr":"0.1","cnt_slr_tot_fdbk_60d":"0.1",' \
                 '"usd_fvf_fee_90d":"0.1","rt_auc_1d_3d_usd_30d":"0.1","rt_alt_shp_opt_lstg_7d":"0.1"} '


class Server(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def do_HEAD(self):
        self._set_headers()

    # GET sends back a Hello world message
    def do_GET(self):
        self._set_headers()
        self.wfile.write(json.dumps({'hello': 'world', 'received': 'ok'}).encode(encoding='utf_8'))

    # POST echoes the message adding a JSON field
    def do_POST(self):
        try:
            ctype, pdict = cgi.parse_header(self.headers.get('content-type'))

            # refuse to receive non-json content
            if ctype != 'application/json':
                self.send_response(400)
                self.end_headers()
                return

            # read the message and convert it into a python dictionary
            length = int(self.headers.get('content-length'))
            message = json.loads(self.rfile.read(length))

            entity_id = int(message['entity_id'])

            if entity_id % 10 > 5:
                self.send_response(400)
                self.end_headers()
            else:
                # send the message back
                self._set_headers()
                self.wfile.write(feature_result.encode(encoding='utf_8'))
        except Exception:
            traceback.print_exc(file=sys.stdout)
            self.send_response(400)
            self.end_headers()


def run(server_class=HTTPServer, handler_class=Server, port=8008):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)

    print('Starting httpd on port %d...' % port)

    httpd.serve_forever()


if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()


