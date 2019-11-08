$(document).ready(
    () => getAccounts()
);

function getAccounts() {
    $.ajax({
        url: 'http://127.0.0.1:8000/api/accounts',
        success: (response) => displayAccounts(response)
    });
}

function displayAccounts(response) {
    let accounts = '';
    response.forEach(
        account => {
            accounts += `<h3>${account.name}</h3><div>${account.industry}</div>`;
        }
    );
    $('#accounts').html(accounts);
}