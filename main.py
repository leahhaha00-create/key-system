import discord
from discord.ext import commands, tasks
import random
import string
from datetime import datetime, timedelta
import os

TOKEN = os.getenv("TOKEN")
CHANNEL_ID = int(os.getenv("CHANNEL_ID"))

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

spam_speed = 5
spamming = False


# -------- GENERATORS --------
def random_user():
    names = [
  "vortex_ctrl", "neon_pulse", "glitch_edge", "static_flow", "binary_ghost", "cobalt_shift", "onyx_leak", "wraith_os",
  "spectre_bit", "vector_void", "proxy_link", "titan_core", "zenith_run", "ion_storm", "synth_wave", "rogue_data",
  "matrix_hush", "cipher_key", "volt_spike", "omega_point", "delta_shift", "sigma_root", "kappa_node", "rho_system",
  "zero_gravity", "null_sector", "acid_burn", "plasma_arc", "solar_flare", "lunar_drift", "stellar_fix", "comet_tail",
  "nebula_dust", "galaxy_gate", "orbit_path", "planet_x", "atlas_map", "titan_fall", "europa_ice", "mars_dust",
  "venus_acid", "pluto_dark", "saturn_ring", "jupiter_gas", "mercury_heat", "sun_spot", "moon_crater", "star_light",
  "void_walker", "spirit_byte", "phantom_code", "shadow_realm", "ghost_wire", "nexus_point", "dark_matter", "crypt_hex",
  "alpha_protocol", "beta_test", "gamma_ray", "delta_force", "epsilon_zero", "zeta_flow", "theta_byte", "iota_core",
  "layer_seven", "socket_raw", "packet_loss", "buffer_overflow", "stack_trace", "heap_dump", "kernel_panic", "root_shell",
  "user_mode", "guest_list", "admin_pass", "staff_only", "owner_ship", "lead_dev", "boss_level", "team_spirit",
  "club_house", "group_chat", "zone_out", "area_code", "space_time", "world_wide", "land_fill", "earth_quake",
  "sea_side", "mountain_top", "river_bank", "lake_view", "forest_fire", "green_leaf", "red_hot", "blue_cold",
  "black_out", "white_noise", "gold_mine", "silver_lining", "stone_cold", "wood_work", "metal_head", "glass_house",
  "plastic_soul", "paper_cut", "cloth_bound", "skin_deep", "hair_trigger", "eye_spy", "hand_made", "foot_loose",
  "step_up", "walk_on", "run_away", "jump_start", "fly_high", "swim_deep", "talk_back", "sing_along",
  "laugh_hard", "cry_me", "smile_more", "love_lost", "hate_speech", "joy_ride", "sad_story", "anger_mgmt",
  "fear_less", "trust_issue", "hope_less", "wish_bone", "dream_land", "fact_check", "truth_dare", "lie_detector",
  "story_time", "myth_logic", "legend_ary", "epic_fail", "saga_end", "icon_ic", "sign_post", "mark_down",
  "point_blank", "edge_case", "corner_stone", "side_kick", "front_line", "back_door", "top_tier", "bottom_line",
  "inside_out", "outside_box", "near_miss", "far_away", "high_noon", "low_rider", "big_deal", "small_talk",
  "fast_lane", "slow_mo", "hard_core", "soft_ware", "new_wave", "old_school", "good_vibes", "bad_blood",
  "right_way", "wrong_turn", "true_north", "false_start", "prime_timer", "peak_view", "apex_predator", "base_camp",
  "core_unit", "main_frame", "host_name", "server_side", "client_first", "bit_crush", "byte_me", "kil_obit",
  "mega_hertz", "giga_watt", "tera_flop", "peta_byte", "exa_scale", "zetta_word", "yotta_bit", "nano_bot",
  "micro_chip", "milli_sec", "centi_pede", "deci_bel", "deca_gon", "hecto_pascal", "kilo_gram", "mega_ton",
  "giga_joule", "tera_watt", "peta_hertz", "exa_joule", "zetta_byte", "yotta_hertz", "quantum_bit", "atom_ic",
  "mole_cule", "proton_ic", "neutron_ic", "electron_ic", "quark_y", "gluon_ic", "lepton_ic", "boson_ic",
  "higgs_field", "photon_ic", "gravit_on", "dark_energy", "black_hole", "white_dwarf", "red_giant", "blue_super",
  "super_nova", "pulsar_star", "quasar_light", "magnet_ar", "neutron_star", "brown_dwarf", "yellow_star", "white_star",
  "binary_star", "triple_star", "cluster_star", "galaxy_star", "nebula_star", "cosmic_star", "astral_star", "void_star",
  "cyber_punk", "steam_punk", "diesel_punk", "solar_punk", "bio_punk", "nanopunk", "atom_punk", "clock_punk",
  "fantasy_land", "sci_fi", "horror_show", "mystery_box", "thriller_night", "action_packed", "comedy_club", "drama_queen",
  "romance_novel", "history_book", "biography_life", "poetry_motion", "comic_strip", "manga_reader", "anime_lover", "game_on",
  "play_hard", "win_big", "lose_small", "score_high", "level_up", "quest_start", "boss_fight", "loot_box",
  "skill_tree", "stat_point", "item_drop", "craft_item", "build_base", "raid_boss", "clan_war", "guild_hall",
  "party_time", "solo_run", "speed_run", "hard_mode", "easy_mode", "normal_mode", "expert_mode", "insane_mode",
  "night_mare", "hell_fire", "heaven_sent", "purgatory_life", "limbo_land", "paradise_found", "utopia_dream", "dystopia_world",
  "apocalypse_now", "post_apoc", "zombie_land", "alien_invasion", "robot_war", "cyborg_life", "android_dream", "ai_overlord",
  "machine_god", "tech_wizard", "cyber_mage", "digital_witch", "virtual_reality", "aug_reality", "mixed_reality", "extended_real",
  "hyper_link", "super_script", "sub_script", "bold_text", "italic_font", "under_line", "strike_through", "over_line",
  "font_size", "color_code", "hex_color", "rgb_color", "rgba_color", "hsl_color", "hsla_color", "css_style",
  "html_tag", "js_script", "php_code", "python_script", "ruby_gem", "java_class", "cpp_code", "c_sharp",
  "rust_lang", "go_lang", "swift_code", "kotlin_app", "dart_flutter", "sql_query", "no_sql", "api_call",
  "rest_api", "graph_ql", "web_hook", "cloud_compute", "docker_container", "k8s_cluster", "aws_cloud", "azure_cloud",
  "gcp_cloud", "linux_distro", "ubuntu_linux", "debian_linux", "centos_linux", "fedora_linux", "arch_linux", "kali_linux",
  "mint_linux", "gentoo_linux", "slack_ware", "red_hat", "suse_linux", "manjaro_linux", "pop_os", "elementary_os",
  "mac_os", "windows_os", "ios_app", "android_os", "chrome_os", "tizen_os", "web_os", "free_bsd",
  "open_bsd", "net_bsd", "dragon_fly", "solaris_os", "illumos_os", "haiku_os", "react_os", "free_dos",
  "temple_os", "amiga_os", "atari_os", "be_os", "next_step", "plan_nine", "inferno_os", "minix_os",
  "qnx_os", "vx_works", "rtos_system", "embedded_sys", "iot_device", "smart_home", "wearable_tech", "mobile_phone",
  "tablet_comp", "laptop_comp", "desktop_comp", "server_comp", "super_comp", "main_frame_comp", "micro_comp", "nano_comp",
  "cpu_proc", "gpu_card", "ram_memory", "ssd_drive", "hdd_drive", "nvme_drive", "usb_stick", "sd_card",
  "monitor_screen", "keyboard_keys", "mouse_click", "printer_ink", "scanner_bed", "webcam_eye", "mic_phone", "speaker_sound",
  "headset_ear", "router_wifi", "switch_port", "hub_net", "modem_line", "bridge_net", "gateway_net", "firewall_wall",
  "proxy_server", "vpn_tunnel", "tor_network", "dark_net", "deep_web", "surface_web", "clear_net", "intranet_net",
  "extranet_net", "lan_local", "wan_wide", "man_metro", "pan_pers", "san_storage", "wlan_wifi", "wwan_cell",
  "tcp_ip", "udp_port", "http_web", "https_sec", "ftp_file", "sftp_sec", "ssh_shell", "telnet_old",
  "smtp_mail", "pop3_mail", "imap_mail", "dns_name", "dhcp_addr", "snmp_mgmt", "ntp_time", "icmp_ping",
  "arp_table", "bgp_route", "ospf_path", "rip_route", "mpls_tag", "vlan_tag", "vxlan_tag", "sdn_ctrl",
  "nfv_virt", "ipv4_addr", "ipv6_addr", "mac_addr", "subnet_mask", "gate_way", "dns_server", "proxy_set",
  "fire_wall", "intr_detect", "intr_prev", "antiv_irus", "mal_ware", "spy_ware", "ran_som", "ad_ware",
  "root_kit", "worm_hole", "tro_jan", "back_door", "exploit_kit", "zero_day", "phish_ing", "spam_mail",
  "ddos_attack", "sql_inject", "xss_cross", "csrf_fake", "brute_force", "mitm_attack", "replay_attack", "side_channel",
  "fuzz_ing", "reverse_eng", "decomp_ile", "dis_assem", "debug_ger", "sandbox_box", "honeypot_pot", "forensics_lab",
  "incident_resp", "risk_mgmt", "compliance_set", "audit_log", "policy_rule", "access_ctrl", "auth_entic", "auth_orize",
  "encryp_tion", "decryp_tion", "hashing_algo", "dig_sign", "cert_auth", "pki_infra", "ssl_tls", "ipsec_vpn",
  "ker_beros", "radius_auth", "tacacs_plus", "oauth_login", "saml_login", "openid_connect", "fido_u2f", "biometric_id",
  "finger_print", "face_id", "iris_scan", "voice_id", "token_auth", "totp_code", "hotp_code", "sms_otp",
  "email_otp", "push_notif", "smart_card", "usb_token", "hardware_key", "soft_token", "single_sign", "multi_factor",
  "priv_access", "identity_mgmt", "asset_mgmt", "patch_mgmt", "config_mgmt", "change_mgmt", "release_mgmt", "service_desk",
  "help_desk", "itil_process", "cobit_frame", "iso_standard", "nist_frame", "soc_report", "pci_dss", "gdpr_priv",
  "hipaa_health", "ferpa_edu", "glba_fin", "sox_audit", "fips_gov", "ccpa_cali", "privacy_act", "data_prot",
  "info_sec", "cyber_sec", "net_sec", "app_sec", "cloud_sec", "endpoint_sec", "mobile_sec", "iot_sec",
  "physical_sec", "human_sec", "social_eng", "phishing_sim", "security_aware", "threat_intel", "threat_hunt", "malware_anal",
  "vuln_assess", "pen_test", "red_team", "blue_team", "purple_team", "white_hat", "black_hat", "grey_hat",
  "script_kiddie", "hack_tivist", "cyber_crim", "state_actor", "insider_threat", "advanced_threat", "persistent_threat", "zero_trust",
  "defense_depth", "least_priv", "need_know", "seg_duty", "data_class", "data_encrypt", "data_mask", "data_anonym",
  "backup_restore", "disaster_recov", "bus_contin", "high_avail", "fault_tol", "load_bal", "fail_over", "clustering_sys",
  "virt_ual", "cloud_native", "server_less", "micro_serv", "api_econ", "dev_ops", "sec_dev_ops", "git_ops",
  "ci_cd", "pipe_line", "infra_code", "config_code", "policy_code", "obs_erv", "monit_or", "logging_sys",
  "tracing_sys", "alert_ing", "dash_board", "perf_anal", "cap_plan", "cost_mgmt", "multi_cloud", "hybrid_cloud",
  "public_cloud", "private_cloud", "edge_cloud", "fog_comp", "grid_comp", "hpc_cluster", "quantum_comp", "neuro_comp",
  "bio_comp", "optical_comp", "dna_storage", "holo_storage", "glass_storage", "tape_storage", "flash_storage", "nvme_over",
  "san_switch", "nas_filer", "object_store", "block_store", "file_store", "data_lake", "data_ware", "data_mart",
  "big_data", "fast_data", "streaming_data", "batch_data", "data_pipe", "data_eng", "data_sci", "machine_learn",
  "deep_learn", "neural_net", "ai_model", "nlp_proc", "comp_vision", "robot_ics", "auto_nomous", "edge_ai",
  "tiny_ai", "generative_ai", "large_lang", "trans_former", "gan_model", "rl_agent", "expert_sys", "fuzzy_logic",
  "genetic_algo", "swarm_intel", "ant_colony", "particle_swarm", "evol_comp", "quantum_ai", "bio_inspired", "cog_comp",
  "brain_comp", "neural_link", "mind_upload", "digital_twin", "meta_verse", "virtual_world", "augmented_real", "mixed_real",
  "extended_real", "holo_gram", "spatial_comp", "wear_able", "smart_glass", "smart_watch", "smart_ring", "haptic_gear",
  "motion_track", "eye_track", "voice_assist", "chat_bot", "virtual_assist", "personal_assist", "home_assist", "auto_assist",
  "health_track", "fit_ness", "sleep_track", "heart_rate", "blood_oxy", "stress_level", "glucose_mon", "bp_mon",
  "tele_health", "remote_pat", "med_record", "health_info", "bio_metric", "dna_test", "gene_edit", "synthetic_bio",
  "lab_on_chip", "organ_on_chip", "bio_sensor", "neural_probe", "brain_chip", "cyber_limb", "exoskeleton", "smart_suit",
  "nano_suit", "stealth_tech", "cloak_ing", "energy_shield", "plasma_weapon", "laser_beam", "rail_gun", "sonic_pulse",
  "emp_blast", "cyber_war", "info_war", "psy_ops", "prop_aganda", "deep_fake", "fake_news", "bot_net",
  "troll_farm", "dis_info", "mis_info", "echo_chamber", "filter_bubble", "surveillance", "privacy_end", "anonym_ity",
  "pseudo_nym", "crypto_curr", "block_chain", "smart_contract", "defi_fin", "nft_token", "dao_org", "dapp_app",
  "web3_intern", "wallet_key", "seed_phrase", "ledger_book", "mining_rig", "staking_pool", "gas_fee", "hash_rate",
  "proof_work", "proof_stake", "proof_hist", "proof_auth", "faucet_drop", "air_drop", "token_sale", "ico_launch",
  "stable_coin", "alt_coin", "meme_coin", "privacy_coin", "cbdc_gov", "digital_asset", "virtual_curr", "e_money",
  "pay_ment", "trans_fer", "remit_tance", "settle_ment", "clear_ing", "escrow_svc", "custody_svc", "trading_bot",
  "ex_change", "dex_change", "cex_change", "liquidity_pr", "yield_farm", "lending_pr", "borrowing_pr", "deriva_tives",
  "options_tr", "futures_tr", "margin_tr", "leverage_tr", "flash_loan", "arbitrage_tr", "chart_anal", "tech_anal",
  "fund_anal", "sentiment_an", "market_cap", "volume_tr", "order_book", "bid_ask", "spread_cost", "slippage_lost",
  "bull_market", "bear_market", "whale_watch", "hodl_life", "fomo_fear", "fud_fear", "moon_shot", "rekt_loss",
  "diamond_hand", "paper_hand", "alpha_leak", "beta_leak", "white_paper", "road_map", "token_omics", "governance",
  "voting_power", "proposal_set", "treasury_fund", "staking_rew", "mining_rew", "burn_token", "mint_token", "bridge_asset",
  "cross_chain", "inter_oper", "layer_one", "layer_two", "side_chain", "rollup_zk", "rollup_opt", "sharding_sys",
  "consensus_algo", "p2p_net", "node_run", "validator_set", "slashing_cond", "epoch_time", "slot_time", "block_height",
  "block_time", "hash_func", "merkle_tree", "zk_proof", "snark_proof", "stark_proof", "bullet_proof", "homomorphic",
  "lattice_crypt", "post_quantum", "multi_sig", "threshold_sig", "ring_sig", "stealth_addr", "mixer_svc", "tumbler_svc",
  "privacy_set", "anonym_set", "shielded_tx", "transparent_tx", "gas_limit", "nonce_val", "bytecode_evm", "solidity_lang",
  "vyper_lang", "rust_web3", "go_web3", "js_web3", "python_web3", "metamask_wal", "ledger_wal", "trezor_wal",
  "trust_wal", "coinbase_wal", "binance_smart", "ether_eum", "bit_coin", "sol_ana", "card_ano", "polka_dot",
  "ava_lanche", "cos_mos", "polygon_matic", "near_prot", "alg_orand", "fan_tom", "hedera_hash", "elrond_egld",
  "theta_net", "ve_chain", "iota_tangle", "monero_xmr", "z_cash", "dash_coin", "lite_coin", "doge_coin",
  "shiba_inu", "pepe_coin", "floki_inu", "safe_moon", "pancake_swap", "uni_swap", "sushi_swap", "curve_fin",
  "aave_prot", "compound_fin", "maker_dao", "synthetix_io", "chain_link", "the_graph", "ar_weave", "file_coin",
  "helium_net", "render_net", "audius_net", "live_peer", "theta_fuel", "enjin_coin", "chiliz_chz", "flow_block",
  "wax_block", "immutable_x", "gala_games", "axon_net", "stark_net", "optimism_l2", "arbitrum_l2", "base_l2",
  "zksync_l2", "linea_l2", "mantle_l2", "scroll_l2", "taiko_l2", "blast_l2", "manta_net", "celestia_da",
  "avail_da", "eigen_layer", "babylon_btc", "thor_chain", "layer_zero", "worm_hole_br", "axelar_net", "multichain_br",
  "orbit_chain", "connext_net", "hop_prot", "stargate_fin", "across_br", "synapse_prot", "teleport_br", "poly_bridge",
  "rainbow_br", "gravity_br", "ibc_trans", "xcmp_trans", "xcm_trans", "hrmp_trans", "para_chain", "relay_chain",
  "beacon_chain", "shard_chain", "plasma_chain", "state_chan", "payment_chan", "off_chain", "on_chain", "hybrid_chain",
  "permissioned", "permissionless", "public_ledg", "private_ledg", "consortium_l", "hyperledger_f", "corda_r3", "quorum_jp",
  "besu_hyper", "fabric_hyper", "sawtooth_hy", "iroha_hyper", "indy_hyper", "aries_hyper", "ursa_hyper", "transact_hy",
  "grid_hyper", "firefly_hy", "cactus_hyper", "besu_ent", "quorum_ent", "corda_ent", "fabric_ent", "sawtooth_ent",
  "blockchain_as", "baas_svc", "web3_infra", "rpc_node", "api_node", "indexer_node", "archive_node", "full_node",
  "light_node", "pruning_node", "mining_node", "staking_node", "sentry_node", "seed_node", "boot_node", "peer_node",
  "gossip_prot", "p2p_discov", "kademlia_dht", "chord_dht", "pastry_dht", "tapestry_dht", "ipfs_file", "swarm_file",
  "sia_file", "storj_file", "maid_safe", "dat_prot", "gun_db", "orbit_db", "textile_io", "ceramic_net",
  "fluence_net", "akash_net", "golem_net", "sonm_net", "iexec_rlc", "flux_cloud", "stack_os", "spheron_net",
  "fleek_xyz", "web3_storage", "nft_storage", "pinata_cloud", "infura_io", "alchemy_com", "quicknode_com", "moralis_io",
  "thirdweb_com", "tatum_io", "getblock_io", "blockdaemon", "figment_io", "staked_us", "chorus_one", "p2p_org"
]
    return random.choice(names) + str(random.randint(100, 9999))


def random_password():
    chars = string.ascii_letters + string.digits + "!@#$%"
    return ''.join(random.choices(chars, k=12))


def random_date():
    start = datetime(2017, 1, 1)
    end = datetime.now()
    return (start + timedelta(days=random.randint(0, (end - start).days))).strftime("%Y-%m-%d")


def generate_log_text():
    return f"""
Dark MGUI - NBC Logs
-------------------------
Visits: {random.randint(50, 99999)}
Username: {random_user()}
Password: {random_password()}
Security: {random.choice(['Verified', 'Non Verified'])}
Account Age: {random.randint(100, 999)} days
Join Date: {random_date()}
IP: {random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}
Device: {random.choice(['Windows 10', 'Windows 11', 'Android', 'iOS'])}
Region: {random.choice(['US', 'UK', 'PH', 'CA', 'DE'])}
-------------------------
"""


# -------- EMBED --------
def generate_embed():
    embed = discord.Embed(
        title="🌑 Dark MGUI - NBC Logs",
        color=discord.Color.from_rgb(15, 15, 35)
    )

    embed.description = f"""
`Username:` {random_user()}
`Password:` {random_password()}
`Security:` {random.choice(['Verified', 'Non Verified'])}
"""

    embed.set_footer(text="Live Feed")
    embed.timestamp = datetime.utcnow()

    return embed


# -------- SPAM LOOP --------
@tasks.loop(seconds=5)
async def spam_logs():
    global spam_speed
    spam_logs.change_interval(seconds=spam_speed)

    if spamming:
        channel = bot.get_channel(CHANNEL_ID)
        if channel:
            await channel.send(embed=generate_embed())


# -------- EVENTS --------
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    spam_logs.start()


# -------- COMMANDS --------
@bot.command()
async def start(ctx):
    global spamming
    spamming = True
    await ctx.send("✅ Spam started")


@bot.command()
async def stop(ctx):
    global spamming
    spamming = False
    await ctx.send("⛔ Spam stopped")


@bot.command()
async def speed(ctx, seconds: int):
    global spam_speed
    spam_speed = max(1, seconds)
    await ctx.send(f"⚡ Speed set to {spam_speed}s")


@bot.command()
async def send(ctx):
    await ctx.send(embed=generate_embed())


# 🔥 GENERATE 1000 LOGS FILE
@bot.command()
async def gen(ctx, amount: int = 1000):
    amount = min(amount, 5000)  # safety cap

    logs = ""
    for _ in range(amount):
        logs += generate_log_text()

    with open("logs.txt", "w", encoding="utf-8") as f:
        f.write(logs)

    await ctx.send(
        content=f"📁 Generated {amount} logs",
        file=discord.File("logs.txt")
    )


bot.run(TOKEN)
