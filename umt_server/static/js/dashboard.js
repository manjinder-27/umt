function renderMonitors(data) {
    const tbody = document.getElementById('monitor-tbody');
    const totalCount = document.getElementById('total-count');
    const upCount = document.getElementById('up-count');
    const downCount = document.getElementById('down-count');

    // Clear loading text
    tbody.innerHTML = '';

    // Update Stats
    totalCount.innerText = data.length;
    upCount.innerText = data.filter(m => m.status === 'Up').length;
    downCount.innerText = data.filter(m => m.status === 'Down').length;

    // Build Rows
    data.forEach(monitor => {
        const row = `
            <tr>
                <td><strong>${monitor.name}</strong></td>
                <td><code>${monitor.url}</code></td>
                <td><span class="badge ${monitor.status}">${monitor.status}</span></td>
                <td>${monitor.latency}</td>
                <td>
                    <button onclick="deleteMonitor(${monitor.id})" class="btn-delete">Delete</button>
                </td>
            </tr>
        `;
        tbody.innerHTML += row;
    });
}

document.addEventListener('DOMContentLoaded', () => {
    fetch('http://127.0.0.1:8000/api/monitors/')
            .then(response => response.json())
            .then(data => renderMonitors(data))
            .catch(error => console.error('Error:', error));
});

function deleteMonitor(id) {
    console.log(`Deleting monitor ${id}...`);
}