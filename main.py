from actions import *
from rdflib import Graph, URIRef, Literal, Namespace
from rdflib.namespace import RDF, RDFS
import subprocess


"""  Create Work Cases (assign work name, form, type, and register license)  """
# wiki_text = register_license(Work('Wikipedia', 'dataset', 'literary'), target_license='CC-BY-SA-4.0') # Corpus, https://en.wikipedia.org/wiki/Wikipedia:Copyrights
#stack_exchange_text = register_license(Work('StackExchange', 'dataset', 'literary'), target_license='CC-BY-SA-4.0') # Corpus, https://stackexchange.com/
free_law_text = register_license(Work('FreeLaw', 'dataset', 'literary'), target_license='CC-BY-ND-4.0') # Corpus, https://free.law/
#arxiv_text = register_license(Work('arXiv', 'dataset', 'literary'), target_license='CC-BY-NC-SA-4.0') # Corpus, https://info.arxiv.org/help/license/index.html
# pubmed_text = register_license(Work('PubMed', 'dataset', 'literary'), target_license='CC-BY-NC-ND-4.0') # Corpus, https://www.ncbi.nlm.nih.gov/pmc/tools/textmining/
#deep_sequoia_text = register_license(Work('Deep-sequoia', 'dataset', 'literary'), target_license='LGPLLR') # Corpus, http://deep-sequoia.inria.fr/

# midjourney_img = register_license(Work('Midjourney_gen', 'dataset', 'vision'), target_license='CC-BY-NC-4.0') # Image, https://docs.midjourney.com/docs/terms-of-service
# flickr_img = register_license(Work('Flickr', 'dataset', 'vision'), target_license='CC-BY-NC-SA-4.0') # Image, https://www.flickr.com/creativecommons/
# stocksnap_img = register_license(Work('StockSnap', 'dataset', 'vision'), target_license='CC0-1.0') # Image, https://stocksnap.io/license
# wikimedia_img = register_license(Work('Wikimedia', 'dataset', 'vision'), target_license='CC-BY-SA-4.0') # Image, https://commons.wikimedia.org/wiki/Main_Page
# open_clipart_img = register_license(Work('OpenClipart', 'dataset', 'vision'), target_license='CC0-1.0') # Image, https://openclipart.org/share

# ccmixter_music = register_license(Work('ccMixter', 'dataset', 'acoustics'), target_license='CC-BY-NC-4.0') # Music, https://ccmixter.org/terms 
# jamendo_music = register_license(Work('Jamendo', 'dataset', 'acoustics'), target_license='CC-BY-NC-ND-4.0') # Music, https://www.jamendo.com/legal/creative-commons

# thingverse_3d = register_license(Work('Thingverse', 'dataset', 'vision'), target_license='CC-BY-NC-SA-4.0') # 3D Model, https://www.thingiverse.com/thing:4850246
# vimeo_video = register_license(Work('Vimeo', 'dataset', 'vision'), target_license='CC-BY-NC-ND-4.0') # Video, https://vimeo.com/creativecommons

# baize_model = register_license(Work('Baize', 'model', 'weights'), target_license='GPL-3.0') # Chatbot, https://github.com/project-baize/baize-chatbot
# stable_diffusion_mode = register_license(Work('StableDiffusion', 'model', 'weights'), target_license='OpenRAIL-M') # Text2Image, https://huggingface.co/runwayml/stable-diffusion-v1-5
# whisper_model = register_license(Work('Whisper', 'model', 'weights'), target_license='MIT') # Voice2Text, https://github.com/openai/whisper
# maskformer_model = register_license(Work('MaskFormer', 'model', 'weights'), target_license='CC-BY-NC-4.0') # Image Segmentation, https://github.com/facebookresearch/MaskFormer/tree/da3e60d85fdeedcb31476b5edd7d328826ce56cc
# detr_model = register_license(Work('DETR', 'model', 'weights'), target_license='Apache-2.0') # Image Segmentation https://github.com/facebookresearch/detr
# xclip_model = register_license(Work('X-Clip', 'model', 'weights'), target_license='MIT') # Video2Text, https://huggingface.co/microsoft/xclip-base-patch32
# i2vgen_model = register_license(Work('I2VGen-XL', 'model', 'weights'), target_license='CC-BY-NC-ND-4.0') # Image2Video, https://huggingface.co/damo-vilab/MS-Image2Video
#bigtranslate_model = register_license(Work('BigTranslate', 'model', 'weights'), target_license='GPL-3.0') # Text Translation, https://huggingface.co/James-WYang/BigTranslate
# bert_model = register_license(Work('BERT', 'model', 'weights'), target_license='Apache-2.0') # Text, https://huggingface.co/bert-base-uncased
# bloom_model = register_license(Work('BLOOM', 'model', 'weights'), target_license='OpenRAIL-M') # Text Generation, https://huggingface.co/bigscience/bloom
# llama2_model = register_license(Work('Llama2', 'model', 'weights'), target_license='Llama2') # Text Generation, https://huggingface.co/meta-llama/Llama-2-7b
ckip_model = register_license(Work('CKIP-Transformers', 'model', 'weights'), target_license='GPL-3.0') # Text Generation, https://github.com/ckiplab/ckip-transformers
phobert_model = register_license(Work('PhoBERT', 'model', 'weights'), target_license='AGPL-3.0') # Text Generation, https://huggingface.co/vinai/phobert-base-v2
#mptchart_model = register_license(Work('MPT-Chat', 'model', 'weights'), target_license='CC-BY-NC-SA-4.0') # Text Generation, https://huggingface.co/mosaicml/mpt-7b-chat
#commandr_model = register_license(Work('C4AI-Command-R+', 'model', 'weights'), target_license='CC-BY-NC-4.0') # Text Generation, https://huggingface.co/CohereForAI/c4ai-command-r-plus-08-2024

#mgbyos_model = register_license(Work('MGBYOS', 'model', 'weights'), target_license='MG-BY-OS')
#mgbync_model = register_license(Work('MGBYNC', 'model', 'weights'), target_license='MG-BY-NC') # MG Licenses


"""  Construct Workflows (use func defined in actions.py)  """
#flow = combine([whisper_model, detr_model])
#flow = combine([embed(arxiv_text, aux_flows=[bigtranslate_model]), embed(stack_exchange_text, aux_flows=[bigtranslate_model]), deep_sequoia_text, free_law_text])

# Case-1
#flow = combine([ckip_model, phobert_model])
#flow = combine([mptchart_model, commandr_model])

flow = generate(combine([ckip_model, phobert_model]), aux_flows=[free_law_text])
#flow = generate(combine([mptchart_model, commandr_model]), aux_flows=[free_law_text])

#flow = phobert_model
#flow = generate(mgbync_model, aux_flows=[free_law_text])
#flow = generate(phobert_model, aux_flows=[free_law_text])
#flow = mgbyos_model
#flow = mgbync_model
#flow = phobert_model

flow = publish(flow, form='literary', policy = 'sell') # literary/service-form
#flow = publish(flow, form='service-form', policy = 'sell') # literary/service-form
# Save the gen graph to a new Turtle file
flow.graph.serialize(destination="gen.ttl", format="ttl")


"""  Reasoning by N3 Rules (complete workflow, dependencies, license determindation)  """
# Workflow Construction
result = subprocess.run(["eye", "--quiet", "--nope", "--pass", 
                         "vocabulary.ttl", "MGLicenseInfo.ttl", "MGLicenseRule.ttl", "gen.ttl",
                         "rules_init.n3", "rules_construct.n3"], 
                         stdout=subprocess.PIPE, check=True)

# Output whole workflow triples, but w/o requests, rulings, and undetermined license of intermediate works.
Graph().parse(data=result.stdout, format="n3").serialize(destination="out_WF.ttl", format="turtle")

# Reasoning: ruling
result = subprocess.run(["eye", "--quiet", "--nope", "--pass", 
                         "vocabulary.ttl", "MGLicenseInfo.ttl", "MGLicenseRule.ttl", "out_WF.ttl",
                         "rules_ruling.n3"], 
                         stdout=subprocess.PIPE, check=True)
# Output WF after 'ruling'
Graph().parse(data=result.stdout, format="n3").serialize(destination="out_WF_ruling.ttl", format="turtle")

# Reasoning: request
result = subprocess.run(["eye", "--quiet", "--nope", "--pass", 
                         "vocabulary.ttl", "MGLicenseInfo.ttl", "MGLicenseRule.ttl", "out_WF_ruling.ttl",
                         "rules_request.n3"], 
                         stdout=subprocess.PIPE, check=True)
# Output WF after 'request'
Graph().parse(data=result.stdout, format="n3").serialize(destination="out_WF_ruling_request.ttl", format="turtle")

"""  Analysis Results (report notice, warnining, error)  """
# Analysis of request
analysis_result = subprocess.run(["eye", "--quiet", "--nope", "--pass-only-new", 
                         "vocabulary.ttl", "MGLicenseInfo.ttl", "MGLicenseRule.ttl", "out_WF_ruling_request.ttl",
                         "rules_analysis_granting.n3"], 
                         stdout=subprocess.PIPE, check=True)

Graph().parse(data=analysis_result.stdout, format="n3").serialize(destination="out_analysis_granting.ttl", format="turtle")

# Analysis of base
analysis_result = subprocess.run(["eye", "--quiet", "--nope", "--pass-only-new", 
                         "vocabulary.ttl", "MGLicenseInfo.ttl", "MGLicenseRule.ttl", "out_WF_ruling_request.ttl",
                         "rules_analysis_base.n3"], 
                         stdout=subprocess.PIPE, check=True)

Graph().parse(data=analysis_result.stdout, format="n3").serialize(destination="out_analysis_base.ttl", format="turtle")

# Analysis of conflicts and reprot restrictions thought rulings.
analysis_result = subprocess.run(["eye", "--quiet", "--nope", "--pass-only-new", 
                         "vocabulary.ttl", "MGLicenseInfo.ttl", "MGLicenseRule.ttl", "out_WF_ruling_request.ttl",
                         "rules_analysis_conflict.n3"], 
                         stdout=subprocess.PIPE, check=True)

Graph().parse(data=analysis_result.stdout, format="n3").serialize(destination="out_analysis_conflict.ttl", format="turtle")


"""  Filter RDF Graphs (for visualization)  """
### Base Workflow Information
filter_result = subprocess.run(["eye", "--quiet", "--nope",
                         "out_WF.ttl", "--query", "filter_base_WF.n3"], 
                         stdout=subprocess.PIPE, check=True)
# Output base workflow triples like input, output and license
Graph().parse(data=filter_result.stdout, format="n3").serialize(destination="out_filter_base_WF.ttl", format="turtle")

### Compositional Dependencies: Mixwork, Subwork, Auxwork
filter_result = subprocess.run(["eye", "--quiet", "--nope",
                         "out_WF.ttl", "--query", "filter_works.n3"], 
                         stdout=subprocess.PIPE, check=True)
# Output Mixwork, Auxwork, Subwork and Provenance relationship triples
Graph().parse(data=filter_result.stdout, format="n3").serialize(destination="out_filter_compositional.ttl", format="turtle")

### Definition Dependencies
filter_result = subprocess.run(["eye", "--quiet", "--nope",
                         "out_WF_ruling.ttl", "--query", "filter_rulings.n3"], 
                         stdout=subprocess.PIPE, check=True)
# Output rulings
Graph().parse(data=filter_result.stdout, format="n3").serialize(destination="out_filter_ruling.ttl", format="turtle")

### Rights-using Dependencies
filter_result = subprocess.run(["eye", "--quiet", "--nope",
                         "out_WF_ruling_request.ttl", "--query", "filter_requests.n3"], 
                         stdout=subprocess.PIPE, check=True)
# Output requests
Graph().parse(data=filter_result.stdout, format="n3").serialize(destination="out_filter_request.ttl", format="turtle")
