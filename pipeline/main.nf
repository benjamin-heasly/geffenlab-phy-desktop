println "params: ${params}"

process geffenlab_phy_desktop {
	tag 'geffenlab_phy_desktop'
	container "ghcr.io/benjamin-heasly/geffenlab-phy-desktop:${params.container_tag}"

    input:
    path exported_path
    
    output:
    path 'results/*', emit: results

    publishDir "${params.results_path}",mode: "copy", overwrite: true, pattern: "results/*", saveAs: { filename -> file(filename).name }

	script:
	"""
	#!/usr/bin/env bash
	set -e
    mkdir -p results
    conda_run python /opt/code/run.py --data-root $exported_path --results-root results
	"""
}

workflow {
    def data = channel.fromPath(params.exported_path)
	geffenlab_phy_desktop(data)
}
