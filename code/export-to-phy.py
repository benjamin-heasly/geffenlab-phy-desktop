import spikeinterface as si
from spikeinterface.exporters import export_to_phy


recording_json = "/data/ecephys/preprocessed/block0_imec0.ap_recording1.json"
bin_dir = "/data/ecephys_1/ecephys/AS20_03112025_trainingSingle6Tone2024_Snk3.1_g0_imec0/"
recording_preprocessed = si.load(recording_json, base_folder=bin_dir)
print(recording_preprocessed)

postprocessed_dir = "/data/ecephys/postprocessed/block0_imec0.ap_recording1.zarr/"
sorting_analyzer = si.load_sorting_analyzer(postprocessed_dir)
print(sorting_analyzer)

# TODO: put sorting analyzer and recording together.

curated_dir = "/data/ecephys/curated/block0_imec0.ap_recording1/"
sorting_curated = si.load(curated_dir)
curated_properties = sorting_curated.get_property_keys()
for property_name in curated_properties:
  property_values = sorting_curated.get_property(property_name)
  sorting_analyzer.set_sorting_property(property_name, property_values)

phy_dir = "/results/ecephys/phy/"
export_to_phy(
  sorting_analyzer=sorting_analyzer,
  output_folder=phy_dir,
  remove_if_exists=True,
  compute_pc_features=False,
  additional_properties=curated_properties
)

