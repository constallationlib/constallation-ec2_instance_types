from instance_type import InstanceType

hpc6a_48xlarge = InstanceType(
    instance_family="hpc6a",
    instance_size="48xlarge",
    free_tier_eligible=False,
    bare_metal=False,
    hypervisor="Nitro",
    vcpus=192,
    architecture="x86_64",
    cores=192,
    valid_cores=[48, 96, 192],
    threads_per_core=1,
    valid_threads_per_core=[1],
    sustained_clock_speed=3.6,
    memory_gb=384.0,
    storage_gb=None,
    storage_type=None,
    network_performance="100 Gigabit",
    instance_storage_gb=None,
    gpu=False,
    gpu_count=0,
    gpu_memory_gb=0,
    eni=20,
    ipv6_support=True
)