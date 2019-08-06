document.addEventListener('DOMContentLoaded', () => {
    function dynaFilters() {
        return new Promise((reject, resolve) => {
            let project = document.getElementById('id_project');
            let filter_by = document.getElementById('id_filter_by');

            if (project.value !== 'CUST') {
                while (filter_by.firstChild) filter_by.removeChild(filter_by.firstChild);
                filter_by.options[filter_by.options.length] = new Option('Fix version', 'fix_version')
            } else {
                while (filter_by.firstChild) filter_by.removeChild(filter_by.firstChild);
                filter_by.options[filter_by.options.length] = new Option('Latest version', 'latest_version')
            }
            resolve();
        })
    }

    // Run when project changes
    document.getElementById('id_project').addEventListener('change', () => {
        dynaFilters();
    });

    // Run every time page loads
    dynaFilters();
});

