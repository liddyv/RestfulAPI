$(document).ready(
    () => {
        addLoginHandler();
    }
);

function addLoginHandler() {
    $('#login').click(
        () => {
            const username = $('#login-username').val();
            const email = $('#login-email').val();
            const password = $('#login-password').val();

            $.post(
                'http://127.0.0.1:8000/auth/login/',
                {
                    username: username,
                    password: password,
                    email: email
                },
                (response) => {
                    const token = response.key;
                    getAccounts(token);
                    hideLogin();
                    addLogoutHandler(token);
                }
            )
        }
    );
}

function getAccounts(token) {
    $.ajax({
        url: 'http://127.0.0.1:8000/api/accounts',
        headers: {
            'Authorization': `Token ${token}`
        },
        success: (response) => {
            displayAccounts(response);
        }
    })
}

function hideLogin() {
    $('#login-username').val(undefined);
    $('#login-email').val(undefined);
    $('#login-password').val(undefined);
    $('#login-form').hide();
}
function showLogin() {
    $('#login-form').show();
}

function displayAccounts(response) {
    let accountCards = '';
    response.forEach(
        (data) => {
            accountCards += `
                    <div class="col s6">
                        <div class="card blue-grey darken-1">
                            <div class="card-content white-text">
                                <span class="card-title">${data.name}</span>
                                <div class="row">
                                    <span class="col s6">Industry</span>
                                    <span class="col s6 right-align">${data.industry}</span>
                                </div>
                            </div>
                        </div>
                    </div>
            `
        }
    )
    $('#accounts').html(`<h3>Accounts</h3><div class="row">${accountCards}</div>`);
}

function addLogoutHandler(token) {
    $('#logout-link').click(
        () => {
            $.ajax({
                url: 'http://127.0.0.1:8000/auth/logout/',
                type: 'post',
                headers: {
                    'Authorization': `Token ${token}`
                },
                success: () => {
                    clearAccounts();
                    showLogin();
                }
            })
        }
    )
}

function clearAccounts() {
    $('#accounts').html('');
}