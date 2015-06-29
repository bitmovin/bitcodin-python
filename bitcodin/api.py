__author__ = 'David Moser <david.moser@bitmovin.net>'

from resource import *
from .rest import RestClient
from .resource import BitcodinObject


def create_input(input_obj):
    """
    Create an Input for bitcodin
    :param input_obj: Input object to create
    :return: Input
    """

    res = RestClient.post(url=get_api_base()+'/input/create', headers=create_headers(), content=input_obj.to_json())

    input_obj = BitcodinObject(res)

    return input_obj


def get_input(input_id=None):
    """
    Get Input information
    :param input_id: The id of the Input to retrieve info from
    :return: BitcodinObject
    """
    url = get_api_base()+'/input/%d' % input_id
    res = RestClient.get(url=url, headers=create_headers())
    input_obj = BitcodinObject(res)

    return input_obj


def list_inputs(page=None):
    """
    Get a list of Inputs
    :param page: number of page to retrieve Inputs from
    :return: list
    """

    if page is None:
        url = get_api_base() + '/inputs'
    else:
        url = get_api_base()+'/inputs/%d' % page

    res = RestClient.get(url=url, headers=create_headers())
    input_obj = BitcodinObject(res)

    return input_obj.inputs


def delete_input(input_id=None):
    """
    Delete an input
    :param input_id: Id of the input to delete
    :return: boolean
    """
    url = get_api_base()+'/input/%d' % input_id
    RestClient.delete(url=url, headers=create_headers())
    return True


def create_encoding_profile(encoding_profile):
    """
    Create an Encoding Profile for bitcodin.

    :param encoding_profile: EncodingProfile: EncodingProfile object to create
    :return: BitcodinObject
    """

    res = RestClient.post(url=get_api_base()+'/encoding-profile/create', headers=create_headers(),
                          content=encoding_profile.to_json())

    encoding_profile = BitcodinObject(res)

    return encoding_profile


def get_encoding_profile(encoding_profile_id=None):
    """
    Get information of an Encoding Profile
    :param encoding_profile_id: The id of the encoding profile to retrieve information from
    :return: BitcodinObject
    """

    url = get_api_base() + '/encoding-profile/%d' % encoding_profile_id
    res = RestClient.get(url=url, headers=create_headers())
    encoding_profile = BitcodinObject(res)

    return encoding_profile


def list_encoding_profiles(page=None):
    """
    List all encoding profiles
    :return: list
    """

    if page is None:
        url = get_api_base() + '/encoding-profiles'
    else:
        url = get_api_base()+'/encoding-profiles/%d' % page

    res = RestClient.get(url=url, headers=create_headers())
    encoding_profile_res = BitcodinObject(res)

    return encoding_profile_res.profiles


def create_job(job):
    """
    Create a Job for bitcodin
    :param: Job: A Job object to create
    :return: BitcodinObject
    """

    res = RestClient.post(url=get_api_base()+'/job/create', headers=create_headers(), content=job.to_json())
    job = BitcodinObject(res)

    return job


def get_job(job_id=None):
    """
    Get information of a Job
    :param job_id: The id of the job to retrieve information from
    :return: Job
    """

    url = get_api_base()+'/job/%d' % job_id

    res = RestClient.get(url=url, headers=create_headers())
    job = BitcodinObject(res)

    return job


def list_jobs(page=None):
    """
    List all Jobs
    :return: list
    """

    if page is None:
        url = get_api_base() + '/jobs'
    else:
        url = get_api_base()+'/jobs/%d' % page

    res = RestClient.get(url=url, headers=create_headers())
    jobs_res = BitcodinObject(res)

    return jobs_res.jobs


def create_output(output):
    """
    Create an output for bitcodin
    :param: Output: A Output object to create
    :return: BitcodinObject
    """

    res = RestClient.post(url=get_api_base()+'/output/create', headers=create_headers(), content=output.to_json())
    output_response = BitcodinObject(res)

    return output_response


def get_output(output_id=None):
    """
    Get information of a output
    :param output_id: The id of the job to retrieve information from
    :return: BitcodinObject
    """

    url = get_api_base()+'/output/%d' % output_id

    res = RestClient.get(url=url, headers=create_headers())
    output_response = BitcodinObject(res)

    return output_response


def list_outputs(page=None):
    """
    List all outputs
    :return: list
    """

    if page is None:
        url = get_api_base() + '/outputs'
    else:
        url = get_api_base()+'/outputs/%d' % page

    res = RestClient.get(url=url, headers=create_headers())
    output_response = BitcodinObject(res)

    return output_response.outputs


def delete_output(output_id=None):
    """
    Delete an output
    :param output_id: The id of the job to delete
    :return: boolean
    """

    url = get_api_base() + '/output/%d' % output_id
    RestClient.delete(url=url, headers=create_headers())
    return True


def get_api_base():
    """
    Get the api base url
    :return: string
    """
    from bitcodin import api_base
    return api_base


def create_headers():
    """
    Create standard headers to communicate with bitcodin-api
    :return:
    """
    from bitcodin import api_key

    if api_key is None:
        raise ValueError("api_key not set. Make sure you have set bitcodin.api_key")

    headers = {
        'Content-Type': 'application/json',
        'bitcodin-api-key': api_key
    }
    return headers

