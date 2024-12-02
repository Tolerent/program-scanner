from flask import Flask, request, jsonify, render_template
from vulnerabilities.sql_injection import detect_sql_injection
from vulnerabilities.toctou import detect_toctou
from vulnerabilities.deserialization import detect_untrusted_deserialization
from vulnerabilities.config_insecurity import detect_insecure_default_config
from vulnerabilities.force_browsing import detect_forced_browsing
from vulnerabilities.debug_info import detect_exposed_debug_info
from vulnerabilities.dead_code import detect_dead_code
from vulnerabilities.auth_check import detect_insufficient_auth_check
from vulnerabilities.stack_trace import detect_leaking_stack_traces
from vulnerabilities.html_css_vulnerabilities import detect_html_css_vulnerabilities
from vulnerabilities.js_vulnerabilities import detect_js_vulnerabilities
from vulnerabilities.unvalidated_json_input import detect_unvalidated_json_input
from vulnerabilities.reverse_tabnabbing import detect_reverse_tabnabbing
from vulnerabilities.weak_hash_functions import detect_weak_hash_functions
from vulnerabilities.cookie_flags import detect_cookie_flags
from vulnerabilities.insecure_websocket import detect_insecure_websocket
from vulnerabilities.eval_usage import detect_eval_usage
from vulnerabilities.insecure_http_methods import detect_insecure_http_methods
from vulnerabilities.session_fixation import detect_session_fixation
from vulnerabilities.http_response_splitting import detect_http_response_splitting
from vulnerabilities.insufficient_entropy import detect_insufficient_entropy
from vulnerabilities.improper_garbage_collection import detect_improper_garbage_collection
from vulnerabilities.cookie_overflow import detect_cookie_overflow
from vulnerabilities.unvalidated_third_party_libraries import detect_unvalidated_third_party_libraries
from vulnerabilities.client_side_caching import detect_client_side_caching
from vulnerabilities.predictable_temp_file_names import detect_predictable_temp_file_names
from vulnerabilities.cryptographic_errors import detect_cryptographic_errors
from vulnerabilities.local_file_inclusion import detect_local_file_inclusion
from vulnerabilities.remote_file_inclusion import detect_remote_file_inclusion
from vulnerabilities.insufficient_account_lockout import detect_insufficient_account_lockout
from vulnerabilities.improper_certificate_validation import detect_improper_certificate_validation
from vulnerabilities.password_in_url import detect_password_in_url
from vulnerabilities.misconfigured_security_headers import detect_misconfigured_security_headers
from vulnerabilities.insecure_api_exposure import detect_insecure_api_exposure
from vulnerabilities.weak_encryption_algorithms import detect_weak_encryption_algorithms
from vulnerabilities.side_channel_attack import detect_side_channel_attack
from vulnerabilities.user_enumeration import detect_user_enumeration
from vulnerabilities.overly_broad_permissions import detect_overly_broad_permissions
from vulnerabilities.unfiltered_file_inclusion import detect_unfiltered_file_inclusion
from vulnerabilities.improper_regex_usage import detect_improper_regex_usage
from vulnerabilities.unrestricted_command_execution import detect_unrestricted_command_execution
from vulnerabilities.environment_variable_exposure import detect_environment_variable_exposure
from vulnerabilities.ui_redress_attack import detect_ui_redress_attack
from vulnerabilities.improper_access_token_usage import detect_improper_access_token_usage
from vulnerabilities.weak_random_seeds import detect_weak_random_seeds
from vulnerabilities.binary_planting import detect_binary_planting
from vulnerabilities.exposed_internal_ips import detect_exposed_internal_ips
from vulnerabilities.excessive_data_exposure import detect_excessive_data_exposure
from vulnerabilities.ssrf import detect_ssrf
from vulnerabilities.shell_metacharacters import detect_shell_metacharacters
from vulnerabilities.clear_text_storage import detect_clear_text_storage
from vulnerabilities.sensitive_data_leak import detect_sensitive_data_leak
from vulnerabilities.improper_sandbox_configuration import detect_improper_sandbox_configuration

app = Flask(__name__)

# Main function to gather all vulnerability checks
def find_vulnerabilities(code):
    issues = []
    issues.extend(detect_sql_injection(code))
    issues.extend(detect_toctou(code))
    issues.extend(detect_untrusted_deserialization(code))
    issues.extend(detect_insecure_default_config(code))
    issues.extend(detect_forced_browsing(code))
    issues.extend(detect_exposed_debug_info(code))
    issues.extend(detect_dead_code(code))
    issues.extend(detect_insufficient_auth_check(code))
    issues.extend(detect_leaking_stack_traces(code))
    issues.extend(detect_html_css_vulnerabilities(code))
    issues.extend(detect_js_vulnerabilities(code))
    issues.extend(detect_unvalidated_json_input(code))
    issues.extend(detect_reverse_tabnabbing(code))
    issues.extend(detect_weak_hash_functions(code))
    issues.extend(detect_cookie_flags(code))
    issues.extend(detect_insecure_websocket(code))
    issues.extend(detect_eval_usage(code))
    issues.extend(detect_insecure_http_methods(code))
    issues.extend(detect_session_fixation(code))
    issues.extend(detect_http_response_splitting(code))
    issues.extend(detect_insufficient_entropy(code))
    issues.extend(detect_improper_garbage_collection(code))
    issues.extend(detect_cookie_overflow(code))
    issues.extend(detect_unvalidated_third_party_libraries(code))
    issues.extend(detect_client_side_caching(code))
    issues.extend(detect_predictable_temp_file_names(code))
    issues.extend(detect_cryptographic_errors(code))
    issues.extend(detect_local_file_inclusion(code))
    issues.extend(detect_remote_file_inclusion(code))
    issues.extend(detect_insufficient_account_lockout(code))
    issues.extend(detect_improper_certificate_validation(code))
    issues.extend(detect_password_in_url(code))
    issues.extend(detect_misconfigured_security_headers(code))
    issues.extend(detect_insecure_api_exposure(code))
    issues.extend(detect_weak_encryption_algorithms(code))
    issues.extend(detect_side_channel_attack(code))
    issues.extend(detect_user_enumeration(code))
    issues.extend(detect_overly_broad_permissions(code))
    issues.extend(detect_unfiltered_file_inclusion(code))
    issues.extend(detect_improper_regex_usage(code))
    issues.extend(detect_unrestricted_command_execution(code))
    issues.extend(detect_environment_variable_exposure(code))
    issues.extend(detect_ui_redress_attack(code))
    issues.extend(detect_improper_access_token_usage(code))
    issues.extend(detect_weak_random_seeds(code))
    issues.extend(detect_binary_planting(code))
    issues.extend(detect_exposed_internal_ips(code))
    issues.extend(detect_excessive_data_exposure(code))
    issues.extend(detect_ssrf(code))
    issues.extend(detect_shell_metacharacters(code))
    issues.extend(detect_clear_text_storage(code))
    issues.extend(detect_sensitive_data_leak(code))
    issues.extend(detect_improper_sandbox_configuration(code))
    return issues

# Render HTML form for code input and file upload on the root route
@app.route('/')
def index():
    return render_template('index.html')  # Render HTML template for the home page

# Endpoint for scanning code submitted via form
@app.route('/scan_code', methods=['POST'])
def scan_code():
    code = ""

    if 'code' in request.form:
        # Handle pasted code from the textarea
        code = request.form['code']
    elif 'file' in request.files:
        # Handle file upload
        uploaded_file = request.files['file']
        if uploaded_file.filename == '':
            return jsonify({"error": "No file selected"}), 400
        code = uploaded_file.read().decode('utf-8')  # Read file contents and decode
    else:
        return jsonify({"error": "No code provided"}), 400

    vulnerabilities = find_vulnerabilities(code)
    return jsonify({"vulnerabilities": vulnerabilities})

if __name__ == '__main__':
    app.run(debug=True)
