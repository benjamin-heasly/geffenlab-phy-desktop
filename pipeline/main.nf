println "params: ${params}"

process geffenlab_phy_desktop {
    tag 'geffenlab_phy_desktop'
    container 'geffenlab/geffenlab-phy-desktop:local'

    input:
    path analysis_path

    output:
    path 'results/*', emit: results

    publishDir "${params.analysis_path}/curated",
        mode: 'copy',
        overwrite: true,
        pattern: 'results/*',
        saveAs: { filename -> file(filename).name }

    script:
    """
    #!/usr/bin/env bash
    set -e
    mkdir -p results
    conda_run python /opt/code/run_phy.py --data-root $analysis_path/exported --results-root results $params.interactive
    """
}

workflow {
    def analysis_channel = channel.fromPath(params.analysis_path)
    geffenlab_phy_desktop(analysis_channel)
}
